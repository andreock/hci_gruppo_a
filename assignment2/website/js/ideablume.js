/* ideaBlume · interazioni del prototipo (miglioramento progressivo).
   Senza JavaScript le pagine restano leggibili; qui si aggiungono menu mobile, date dimostrative,
   filtri, ricerca, FAQ, spiegazioni a comparsa, donazione simulata e validazione dei moduli.
   Nessuna richiesta di rete: tutti i dati sono in data/ib-dati.js. */
(function () {
  "use strict";

  var LANG = document.documentElement.lang === "en" ? "en" : "it";
  var D = window.IB_DATI || null;      // dati dei progetti: solo nelle pagine che ne hanno bisogno
  var I = window.IB_TESTI || null;     // testi dell'interfaccia nella lingua della pagina: in tutte le pagine
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- utilità ---------- */
  function store(k, v) {                       // sessionStorage protetto (modalità privata, file://)
    try {
      if (v === undefined) return JSON.parse(sessionStorage.getItem(k) || "null");
      if (v === null) sessionStorage.removeItem(k); else sessionStorage.setItem(k, JSON.stringify(v));
    } catch (e) { return null; }
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function oggi() { var d = new Date(); return new Date(d.getFullYear(), d.getMonth(), d.getDate()); }
  function dataDa(spec) {
    if (spec.indexOf("rel:") === 0) { var d = oggi(); d.setDate(d.getDate() + parseInt(spec.slice(4), 10)); return d; }
    var p = spec.split("-"); return new Date(+p[0], +p[1] - 1, +p[2]);
  }
  var MESI_IT = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"];
  function fmtData(d, lunga) {
    var mesi = I ? I.mesi : MESI_IT;
    if (LANG === "it") {
      if (lunga) return d.getDate() + " " + mesi[d.getMonth()] + " " + d.getFullYear();
      return ("0" + d.getDate()).slice(-2) + "/" + ("0" + (d.getMonth() + 1)).slice(-2) + "/" + d.getFullYear();
    }
    return d.getDate() + " " + (I ? mesi[d.getMonth()] : ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][d.getMonth()]) + " " + d.getFullYear();
  }
  function iso(d) { return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); }
  function euro(x) {
    var intero = Math.abs(x - Math.round(x)) < 1e-9;
    var s = x.toLocaleString(LANG === "it" ? "it-IT" : "en-GB", { minimumFractionDigits: intero ? 0 : 2, maximumFractionDigits: intero ? 0 : 2, useGrouping: true });
    if (LANG === "it" && x >= 1000 && x < 10000 && s.indexOf(".") < 0) s = s.replace(/^(\d)(\d{3})/, "$1.$2"); // it-IT non raggruppa le migliaia sotto 10.000
    return LANG === "it" ? "€ " + s : "€" + s;
  }
  function tpl(s, v) {                        // stesse convenzioni di tools/build.py
    v = v || {};
    var ctx = I ? I.ctx : {};
    s = s.replace(/\{link:([^|}]+)\|([^}]+)\}/g, function (m, u, t) { return '<a href="' + esc(u) + '">' + t + "</a>"; });
    s = s.replace(/\{DV\}/g, I ? '<span class="placeholder">' + esc(I.placeholder) + "</span>" : "");
    return s.replace(/\{([a-z_]+)\}/g, function (m, k) { return k in v ? v[k] : (k in ctx ? ctx[k] : m); });
  }
  function annuncia(el, html) { if (el) { el.innerHTML = ""; window.setTimeout(function () { el.innerHTML = html; }, 50); } }

  /* ---------- date dimostrative (D-24, D-27) ---------- */
  $$("time[data-rel]").forEach(function (t) {
    var d = oggi(); d.setDate(d.getDate() + parseInt(t.getAttribute("data-rel"), 10));
    t.setAttribute("datetime", iso(d));
    t.textContent = fmtData(d, t.hasAttribute("data-lunga"));
  });

  /* ---------- menu mobile (P-008, P-085) ---------- */
  var toggle = $("[data-nav-toggle]"), nav = $("#menu-principale");
  if (toggle && nav) {
    var mq = window.matchMedia("(max-width: 899px)");
    var label = $("[data-nav-label]", toggle);
    var imposta = function (aperto) {
      toggle.setAttribute("aria-expanded", aperto ? "true" : "false");
      if (label && I) label.textContent = aperto ? I.js.menu_close : I.js.menu_open;
      nav.hidden = mq.matches && !aperto;
    };
    imposta(false);
    toggle.addEventListener("click", function () {
      var aperto = toggle.getAttribute("aria-expanded") !== "true";
      imposta(aperto);
      if (aperto) { var primo = $("a", nav); if (primo) primo.focus(); }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && mq.matches && toggle.getAttribute("aria-expanded") === "true") { imposta(false); toggle.focus(); }
    });
    (mq.addEventListener ? mq.addEventListener.bind(mq, "change") : mq.addListener.bind(mq))(function () { imposta(false); });
  }

  /* ---------- selettore di lingua: stessa pagina, stessi filtri e ancora (R-112) ---------- */
  $$("[data-lang-switch]").forEach(function (a) {
    a.addEventListener("click", function () { a.href = a.href.split(/[?#]/)[0] + location.search + location.hash; });
  });

  /* ---------- spiegazioni a comparsa: pulsante, Esc, nessun link a "#" (P-044) ---------- */
  $$("[data-toggletip]").forEach(function (box) {
    var btn = $("button", box), panel = $("[data-toggletip-panel]", box);
    panel.hidden = true;
    btn.addEventListener("click", function () {
      var aperto = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", aperto ? "false" : "true"); panel.hidden = aperto;
    });
    box.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !panel.hidden) { panel.hidden = true; btn.setAttribute("aria-expanded", "false"); btn.focus(); }
    });
  });

  /* ---------- copia link ---------- */
  $$("[data-copia]").forEach(function (b) {
    var esito = $("[data-copia-esito]");
    b.addEventListener("click", function () {
      var ok = function () { annuncia(esito, esc(b.getAttribute("data-ok"))); };
      var ko = function () { annuncia(esito, esc(b.getAttribute("data-ko"))); };
      if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(location.href.split("#")[0]).then(ok, ko);
      else {
        var ta = document.createElement("textarea"); ta.value = location.href.split("#")[0]; ta.setAttribute("readonly", "");
        ta.style.position = "absolute"; ta.style.left = "-9999px"; document.body.appendChild(ta); ta.select();
        try { document.execCommand("copy") ? ok() : ko(); } catch (e) { ko(); }
        document.body.removeChild(ta);
      }
    });
  });

  $$("[data-stampa]").forEach(function (b) { b.addEventListener("click", function () { window.print(); }); });

  /* ---------- validazione dei moduli (P-054, P-059, P-073, P-077) ---------- */
  var RE_EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  var RE_TEL = /^\+?[\d\s]{6,}$/;
  function msg(k, v) { return I ? tpl(I.js[k], v) : ""; }
  function numero(s) { s = String(s).trim().replace(/\s/g, "").replace("€", ""); if (!s) return NaN; s = s.replace(/\./g, "").replace(",", "."); return /^\d+(\.\d{1,2})?$/.test(s) ? parseFloat(s) : NaN; }

  function controlla(el) {
    if (el.closest("[hidden]")) return "";
    var v = (el.value || "").trim();
    if (el.type === "checkbox") return el.required && !el.checked ? msg(el.id.indexOf("privacy") >= 0 ? "err_privacy" : "err_consent") : "";
    if (el.type === "radio") return "";
    if (el.required && !v) return el.tagName === "SELECT" ? msg("err_select") : msg(el.getAttribute("data-err") || "err_required");
    if (!v) return "";
    if (el.type === "email" && !RE_EMAIL.test(v)) return msg("err_email");
    if (el.type === "tel" && !RE_TEL.test(v)) return msg("err_tel");
    if (el.hasAttribute("data-conta") && v.length > +el.getAttribute("data-conta")) return msg("err_maxlen", { n: v.length, max: el.getAttribute("data-conta") });
    if (el.hasAttribute("data-obiettivo")) { var n = numero(v); if (isNaN(n)) return msg("err_amount_nan"); if (n < 3000 || n > 10000) return msg("err_goal"); }
    if (el.hasAttribute("data-min")) {
      var x = numero(v), min = +el.getAttribute("data-min");
      if (isNaN(x)) return msg("err_amount_nan");
      if (x < min) return msg("err_amount_min", { min: euro(min), minnum: String(min) });
    }
    return "";
  }
  function controllaGruppo(fs) {
    if (fs.closest("[hidden]")) return "";
    if ($("input:checked", fs)) return "";
    return msg({ scelta: "err_choice", visibilita: "err_visibility", metodo: "err_method" }[fs.getAttribute("data-gruppo")] || "err_required");
  }
  function mostraErrore(target, testo, ancora) {
    var cont = target.matches("fieldset") ? target : target.closest(".field") || target.parentNode;
    var id = (target.id || target.getAttribute("data-gruppo")) + "-e";
    var p = document.getElementById(id);
    if (!p) {
      p = document.createElement("p"); p.className = "field-error"; p.id = id;
      if (target.matches("fieldset")) $("legend", target).insertAdjacentElement("afterend", p); else cont.appendChild(p);
    }
    var campi = target.matches("fieldset") ? $$("input", target) : [target];
    if (testo) {
      p.textContent = testo; p.hidden = false; cont.classList.add("field--error");
      campi.forEach(function (c) {
        c.setAttribute("aria-invalid", "true");
        var db = (c.getAttribute("aria-describedby") || "").split(" ").filter(Boolean);
        if (db.indexOf(id) < 0) { db.push(id); c.setAttribute("aria-describedby", db.join(" ")); }
      });
    } else {
      p.hidden = true; p.textContent = ""; cont.classList.remove("field--error");
      campi.forEach(function (c) { c.removeAttribute("aria-invalid"); });
    }
    return ancora;
  }
  function etichetta(el) {
    if (el.matches("fieldset")) return $("legend", el).textContent.trim();
    var l = document.querySelector('label[for="' + el.id + '"]');
    return l ? l.textContent.replace(/\(.*\)/, "").trim() : el.name;
  }
  function validaAmbito(ambito) {                // restituisce l'elenco degli errori e li mostra accanto ai campi
    var errori = [];
    $$("input:not([type=radio]), select, textarea", ambito).forEach(function (el) {
      var m = controlla(el); mostraErrore(el, m); if (m) errori.push({ el: el, m: m });
    });
    $$("fieldset[data-gruppo]", ambito).forEach(function (fs) {
      var m = controllaGruppo(fs); mostraErrore(fs, m); if (m) errori.push({ el: fs, m: m });
    });
    return errori;
  }
  function riepilogoErrori(box, errori) {
    if (!box) return;
    if (!errori.length) { box.hidden = true; return; }
    $("[data-errori-titolo]", box).textContent = errori.length === 1 ? msg("err_title_1") : msg("err_title_n", { n: errori.length });
    $("[data-errori-lista]", box).innerHTML = errori.map(function (e) {
      var id = e.el.matches("fieldset") ? $("input", e.el).id : e.el.id;
      return '<li><a href="#' + id + '">' + esc(etichetta(e.el)) + "</a>: " + esc(e.m) + "</li>";
    }).join("");
    box.hidden = false; box.focus();
    $$("a", box).forEach(function (a) {
      a.addEventListener("click", function (ev) { ev.preventDefault(); var t = document.getElementById(a.getAttribute("href").slice(1)); if (t) t.focus(); });
    });
  }
  function collegaValidazione(form) {
    form.addEventListener("focusout", function (e) {              // all'uscita dal campo
      var el = e.target;
      if (!el.matches || !el.matches("input, select, textarea")) return;
      if (el.type === "radio") { var fs = el.closest("fieldset[data-gruppo]"); if (fs && !fs.contains(e.relatedTarget)) mostraErrore(fs, controllaGruppo(fs)); return; }
      if (el.value || el.getAttribute("aria-invalid")) mostraErrore(el, controlla(el));
    });
    form.addEventListener("input", function (e) {                 // l'errore sparisce appena il valore è corretto
      var el = e.target;
      if (el.getAttribute && el.getAttribute("aria-invalid") === "true" && !controlla(el)) mostraErrore(el, "");
    });
    form.addEventListener("change", function (e) {
      var el = e.target;
      if (el.type === "radio" || el.type === "checkbox") {
        var fs = el.closest("fieldset[data-gruppo]");
        if (fs) mostraErrore(fs, controllaGruppo(fs)); else if (el.getAttribute("aria-invalid")) mostraErrore(el, controlla(el));
      }
      if (el.tagName === "SELECT" && el.getAttribute("aria-invalid")) mostraErrore(el, controlla(el));
    });
  }
  function bozza(form) {                                          // i dati restano se si torna indietro (WCAG 3.3.7)
    var k = form.getAttribute("data-salva"); if (!k) return;
    var s = store(k) || {};
    $$("input, select, textarea", form).forEach(function (el) {
      if (!(el.name in s)) return;
      if (el.type === "checkbox") el.checked = !!s[el.name]; else if (el.type === "radio") el.checked = s[el.name] === el.value; else el.value = s[el.name];
    });
    form.addEventListener("input", function () {
      var o = {};
      $$("input, select, textarea", form).forEach(function (el) {
        if (el.type === "checkbox") o[el.name] = el.checked; else if (el.type === "radio") { if (el.checked) o[el.name] = el.value; } else o[el.name] = el.value;
      });
      store(k, o);
    });
  }
  function contatori(form) {
    $$("[data-conta]", form).forEach(function (el) {
      var max = el.getAttribute("data-conta"), p = document.createElement("p");
      p.className = "small muted"; p.id = el.id + "-c"; el.insertAdjacentElement("afterend", p);
      var agg = function () { p.textContent = msg("chars", { n: el.value.length, max: max }); };
      el.addEventListener("input", agg); agg();
    });
  }
  function invioSimulato(btn, fatto) {
    var testo = btn.textContent;
    btn.setAttribute("aria-busy", "true"); btn.disabled = true;
    if (btn.getAttribute("data-label-invio")) btn.textContent = btn.getAttribute("data-label-invio");
    window.setTimeout(function () { btn.removeAttribute("aria-busy"); btn.disabled = false; btn.textContent = testo; fatto(); }, 900);
  }

  /* ---------- moduli semplici: contatti, candidatura, collaborazione, scrivi al gruppo ---------- */
  $$("form[data-form]").forEach(function (form) {
    var tipo = form.getAttribute("data-form");
    if (tipo === "donazione") return;
    collegaValidazione(form); bozza(form); contatori(form);
    var box = form.parentNode.querySelector("[data-errori]");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var errori = validaAmbito(form);
      if (errori.length) { if (box) riepilogoErrori(box, errori); else errori[0].el.focus(); return; }
      if (box) box.hidden = true;
      var btn = $("button[type=submit]", form);
      invioSimulato(btn, function () {
        var val = function (n) { var el = form.elements[n]; return el ? el.value.trim() : ""; };
        if (tipo === "scrivi") {
          var ok = form.parentNode.querySelector("[data-scrivi-ok]");
          form.hidden = true; ok.hidden = false;
          annuncia(ok, "<p>" + tpl(I.progetto.form_sent, { giorni: form.getAttribute("data-giorni") }) + "</p>");
          ok.setAttribute("tabindex", "-1"); ok.focus();
          return;
        }
        var fin = form.parentNode.querySelector("[data-inviato]");
        if (tipo === "contatti") {
          $("[data-inviato-testo]", fin).innerHTML = tpl(I.contatti.f_sent, { giorni: form.getAttribute("data-giorni"), email: esc(val("ct-email")) });
        } else {
          var g = tipo === "candidatura" ? I.candidatura : I.collabora;
          var tel = val("k-telefono");
          $("[data-inviato-testo]", fin).innerHTML = tpl(g.sent, { nome: esc(val("c-nome")), email: esc(val(tipo === "candidatura" ? "c-email" : "k-email")), tel: tel ? " / " + esc(tel) : "" });
          $("[data-inviato-riepilogo]", fin).innerHTML = $$("input, select, textarea", form).filter(function (el) { return el.type !== "checkbox" && el.value.trim(); })
            .map(function (el) { var v = el.tagName === "SELECT" ? el.options[el.selectedIndex].text : el.value; return "<dt>" + esc(etichetta(el)) + "</dt><dd>" + esc(v).replace(/\n/g, "<br>") + "</dd>"; }).join("");
          store(form.getAttribute("data-salva"), null);
        }
        form.hidden = true; fin.hidden = false; fin.focus();
      });
    });
  });

  /* Scrivi al gruppo: indicatore e conferma immediata (P-039) */
  var apri = $("[data-scrivi-apri]"), scrivi = $("[data-scrivi]");
  if (apri && scrivi) {
    apri.addEventListener("click", function () {
      var aperto = apri.getAttribute("aria-expanded") === "true";
      apri.setAttribute("aria-expanded", aperto ? "false" : "true"); scrivi.hidden = aperto;
      if (!aperto) $("input", scrivi).focus();
    });
    $("[data-scrivi-annulla]", scrivi).addEventListener("click", function () { scrivi.hidden = true; apri.setAttribute("aria-expanded", "false"); apri.focus(); });
  }

  /* ---------- stato di un progetto (stessa logica di tools/build.py, R-022) ---------- */
  function calcola(p) {
    var scad = dataDa(p.scadenza), giorni = Math.round((scad - oggi()) / 864e5), ragg = p.raccolto >= p.obiettivo;
    var stato = giorni < 0 ? (ragg ? "done" : "failed") : (ragg ? "reached" : "open");
    var sost = p.ricompense.reduce(function (a, r) { return a + r.scelte; }, 0) + p.libere;
    return { scad: scad, giorni: giorni, stato: stato, perc: 100 * p.raccolto / p.obiettivo, aperto: giorni >= 0, sost: sost };
  }
  var ICONE = {
    open: '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-width="2"/></svg>',
    reached: '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M3 8.5l3.2 3L13 4.5" fill="none" stroke="currentColor" stroke-width="2.4"/></svg>',
    done: '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><rect x="3" y="3" width="10" height="10" fill="currentColor"/></svg>',
    failed: '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M4 4l8 8M12 4l-8 8" stroke="currentColor" stroke-width="2.4"/></svg>'
  };
  function statoHtml(p, c) {
    var testo;
    if (c.stato === "open" || c.stato === "reached") {
      var k = c.giorni > 1 ? c.stato : c.stato + "_" + c.giorni;
      testo = tpl(I.status[k], { n: c.giorni, data: '<time datetime="' + iso(c.scad) + '">' + fmtData(c.scad) + "</time>" });
    } else testo = esc(I.status[c.stato]);
    return '<span class="status status--' + c.stato + '">' + ICONE[c.stato] + "<span>" + testo + "</span></span>";
  }
  function cardHtml(p) {
    var c = calcola(p), prefix = LANG === "en" ? "../" : "";
    var dip = D.sito.dipartimenti[p.dipartimento][LANG], cat = D.sito.categorie[p.categoria][LANG];
    return '<li><article class="card"><div class="card__media"><img src="' + prefix + "img/progetti/" + p.slug + '.svg" alt="" width="320" height="180" loading="lazy"></div>' +
      '<div class="card__body"><p class="card__meta"><span class="tag">' + esc(cat) + "</span> · " + esc(tpl(I.card.anno, { anno: p.anno })) +
      (p.programma ? ' · <span class="tag">' + esc(I.card.programma) + "</span>" : "") + "</p>" +
      '<h3 class="card__title"><a href="progetto-' + p.slug + '.html">' + esc(p.titolo[LANG]) + "</a></h3>" +
      '<p class="card__org">' + tpl(I.card.org, { gruppo: esc(p.gruppo), dip: esc(dip) }) + "</p><p>" + statoHtml(p, c) + "</p>" +
      '<div class="progress" aria-hidden="true"><div class="progress__bar" style="width:' + Math.min(100, c.perc).toFixed(0) + '%"></div></div>' +
      '<p class="card__figures">' + tpl(I.card.raised, { raccolto: euro(p.raccolto), obiettivo: euro(p.obiettivo), perc: Math.round(c.perc) + "%" }) + " · " + tpl(I.card.supporters, { n: c.sost }) + "</p></div></article></li>";
  }

  /* ---------- elenco dei progetti: filtri nella URL, conteggio, posizione (P-027, P-031–P-033) ---------- */
  var formFiltri = $("[data-filtri]");
  if (formFiltri && D) {
    var elenco = $("[data-elenco]"), items = $$("li[data-slug]", elenco);
    var conteggio = $("[data-conteggio]"), nessuno = $("[data-nessuno]"), fine = $("[data-fine]");
    var campi = ["stato", "categoria", "dip", "anno", "programma", "ordina"];
    var leggi = function () { var q = new URLSearchParams(location.search); campi.forEach(function (k) { var s = formFiltri.elements[k]; if (s) s.value = q.get(k) || ""; }); };
    var applica = function (annunciare) {
      var f = {}; campi.forEach(function (k) { f[k] = formFiltri.elements[k].value; });
      var vis = items.filter(function (li) {
        var st = li.getAttribute("data-stato");
        if (f.stato === "in-corso" && !(st === "open" || st === "reached")) return false;
        if (f.stato === "raggiunto" && st !== "reached") return false;
        if (f.stato === "conclusi" && !(st === "done" || st === "failed")) return false;
        if (f.categoria && li.getAttribute("data-cat") !== f.categoria) return false;
        if (f.dip && li.getAttribute("data-dip") !== f.dip) return false;
        if (f.anno && li.getAttribute("data-anno") !== f.anno) return false;
        if (f.programma && li.getAttribute("data-prog") !== f.programma) return false;
        return true;
      });
      var aperto = function (li) { var s = li.getAttribute("data-stato"); return s === "open" || s === "reached"; };
      var scad = function (li) { return dataDa(li.getAttribute("data-scadenza")).getTime(); };
      var perc = function (li) { return parseFloat(li.getAttribute("data-perc")); };
      var cmp = {
        "": function (a, b) { return aperto(b) - aperto(a) || (aperto(a) ? scad(a) - scad(b) : scad(b) - scad(a)); },
        recenti: function (a, b) { return dataDa(b.getAttribute("data-inizio")) - dataDa(a.getAttribute("data-inizio")); },
        bisogno: function (a, b) { return aperto(b) - aperto(a) || perc(a) - perc(b); },
        percentuale: function (a, b) { return aperto(b) - aperto(a) || perc(b) - perc(a); }
      }[f.ordina] || function () { return 0; };
      items.forEach(function (li) { li.hidden = true; });
      vis.sort(cmp).forEach(function (li) { li.hidden = false; elenco.appendChild(li); });
      var t = tpl(I.progetti.count, { n: vis.length, tot: items.length });
      if (annunciare) annuncia(conteggio, esc(t)); else conteggio.textContent = t;
      nessuno.hidden = vis.length > 0; fine.hidden = vis.length === 0;
      var q = new URLSearchParams(); campi.forEach(function (k) { if (f[k]) q.set(k, f[k]); });
      history.replaceState(history.state, "", location.pathname + (q.toString() ? "?" + q : ""));
    };
    leggi(); applica(false);
    formFiltri.addEventListener("change", function () { applica(true); });
    formFiltri.addEventListener("submit", function (e) { e.preventDefault(); applica(true); });
    $("[data-reset]", formFiltri).addEventListener("click", function (e) { e.preventDefault(); formFiltri.reset(); campi.forEach(function (k) { formFiltri.elements[k].value = ""; }); applica(true); formFiltri.elements.stato.focus(); });
    var chiave = function () { return "ib-scroll:" + location.pathname + location.search; };
    elenco.addEventListener("click", function (e) { if (e.target.closest("a")) store(chiave(), window.scrollY); });
    var y = store(chiave()); if (y) window.scrollTo(0, y);
    window.addEventListener("pageshow", function (e) { if (e.persisted) { leggi(); applica(false); } });
  }

  /* ---------- ricerca (P-005, P-006) ---------- */
  var risultati = $("[data-risultati]");
  if (risultati && D) {
    var norm = function (s) { return String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); };
    var q = (new URLSearchParams(location.search).get("q") || "").trim();
    var campo = $("#q-cerca"); campo.value = q;
    var titolo = $("[data-risultati-titolo]");
    if (q) {
      var parole = norm(q).split(/\s+/).filter(Boolean);
      var trovati = D.progetti.filter(function (p) {
        var testo = norm([p.titolo[LANG], p.sottotitolo[LANG], p.testo[LANG], p.gruppo, p.anno, D.sito.categorie[p.categoria][LANG],
          D.sito.dipartimenti[p.dipartimento][LANG], p.titolo.it, p.titolo.en].join(" "));
        return parole.every(function (w) { return testo.indexOf(w) >= 0; });
      }).sort(function (a, b) { return calcola(b).aperto - calcola(a).aperto; });
      risultati.innerHTML = trovati.map(cardHtml).join("");
      var t = trovati.length === 0 ? I.cerca.none_title : trovati.length === 1 ? I.cerca.result_1 : I.cerca.result_n;
      titolo.textContent = tpl(t, { n: trovati.length, q: q });
      $("[data-nessun-risultato]").hidden = trovati.length > 0;
      var pag = D.pagine[LANG].filter(function (pg) { var tx = norm(pg.titolo + " " + pg.testo); return parole.some(function (w) { return w.length > 2 && tx.indexOf(w) >= 0; }); });
      if (pag.length) {
        $("[data-pagine-sito]").hidden = false;
        $("[data-pagine-titolo]").textContent = tpl(I.cerca.pages_title, { q: q });
        $("[data-pagine-elenco]").innerHTML = pag.map(function (pg) { return '<li><a href="' + pg.url + '">' + esc(pg.titolo) + "</a></li>"; }).join("");
      }
      document.title = titolo.textContent + " – ideaBlume";
    } else { campo.focus(); }
  }

  /* ---------- FAQ: ricerca interna e ancore condivisibili (P-075) ---------- */
  var faqCerca = $("[data-faq-cerca]");
  function apriAncora() {
    var id = decodeURIComponent(location.hash.slice(1)); if (!id) return;
    var d = document.getElementById(id);
    if (d && d.tagName === "DETAILS") {
      $$("details.is-target").forEach(function (x) { x.classList.remove("is-target"); });
      d.open = true; d.classList.add("is-target"); $("summary", d).focus();
    }
  }
  if ($("[data-faq-gruppo]") && I) {
    apriAncora(); window.addEventListener("hashchange", apriAncora);
    var cont = $("[data-faq-conteggio]");
    if (faqCerca) faqCerca.addEventListener("input", function () {
      var w = faqCerca.value.trim().toLowerCase(), n = 0;
      $$("[data-faq-gruppo] details").forEach(function (d) {
        var ok = !w || d.textContent.toLowerCase().indexOf(w) >= 0; d.hidden = !ok; if (ok) n++;
      });
      $$("[data-faq-gruppo] .accordion").forEach(function (a) { var vis = $$("details:not([hidden])", a).length > 0; a.hidden = !vis; a.previousElementSibling.hidden = !vis; });
      $$("[data-faq-gruppo]").forEach(function (s) { s.hidden = $$("details:not([hidden])", s).length === 0; });
      cont.innerHTML = w ? tpl(n === 0 ? I.faq.count_0 : n === 1 ? I.faq.count_1 : I.faq.count_n, { n: n }) : "";
    });
  }

  /* ---------- donazione simulata in 5 passi (P-054–P-063) ---------- */
  var app = $("[data-don-app]");
  if (app && D) donazione();

  function donazione() {
    var G = I.don, params = new URLSearchParams(location.search);
    var p = D.progetti.filter(function (x) { return x.slug === params.get("progetto"); })[0];
    var assente = $("[data-don-assente]");
    if (!p || !calcola(p).aperto) {
      assente.hidden = false;
      $("[data-don-assente-testo]", assente).textContent = p ? G.closed : G.missing;
      $("[data-don-assente-azioni]", assente).innerHTML = (p ? '<a class="btn btn--secondary" href="progetto-' + p.slug + '.html">' + esc(G.back_project) + "</a>" : "") +
        '<a class="btn" href="progetti.html?stato=in-corso">' + esc(p ? G.closed_cta : G.missing_cta) + "</a>";
      return;
    }
    var c = calcola(p), form = $("form[data-form=donazione]"), KEY = "ib-don-" + p.slug;
    var s = store(KEY) || {};
    if (params.get("ricompensa")) s.scelta = params.get("ricompensa");
    var tot = 5, titoloBreve = p.titolo_breve[LANG];
    document.title = tpl(G.title_project, { titolo: titoloBreve });
    $("[data-don-titolo]").textContent = tpl(G.h1_project, { titolo: p.titolo[LANG] });
    $("[data-torna-progetto]").href = "progetto-" + p.slug + ".html";
    app.hidden = false;

    // passo 1: scelte
    var minLib = D.sito.regole.minimo_libero;
    var scelte = [{ id: "libera", importo: minLib, titolo: G.sum_free, desc: "" }]
      .concat(p.ricompense.filter(function (r) { return !r.posti || r.posti - r.scelte > 0; }).sort(function (a, b) { return a.importo - b.importo; })
        .map(function (r) { return { id: r.id, importo: r.importo, titolo: r.titolo[LANG], desc: r.descrizione[LANG] }; }));
    $("[data-scelte]").innerHTML = scelte.map(function (r) {
      var prezzo = r.id === "libera" ? tpl(I.progetto.from, { importo: euro(r.importo) }) : euro(r.importo);
      return '<label class="choice" for="sc-' + r.id + '"><input id="sc-' + r.id + '" type="radio" name="scelta" value="' + r.id + '" required>' +
        '<span class="choice__text"><strong>' + esc(prezzo) + "</strong> · " + esc(r.titolo) + (r.id !== "libera" ? "<small>" + esc(r.desc) + "</small>" : "") + "</span></label>";
    }).join("");
    var importo = $("#importo");
    var raddoppio = $("[data-s1-raddoppio]");
    raddoppio.innerHTML = !p.programma ? esc(G.s1_no_match) : (c.stato === "reached" ? tpl(G.s1_match_over) : tpl(G.s1_match));
    var scelta = function () { var r = $("input[name=scelta]:checked", form); return r ? scelte.filter(function (x) { return x.id === r.value; })[0] : null; };
    var aggiornaMin = function (forza) {
      var r = scelta(), min = r ? r.importo : minLib;
      importo.setAttribute("data-min", min);
      $("[data-importo-hint]").textContent = tpl(G.s1_amount_hint, { min: euro(min) });
      var n = numero(importo.value);
      if (r && (forza || isNaN(n) || n < min)) importo.value = String(min).replace(".", LANG === "it" ? "," : ".");
    };

    // ripristino della bozza
    var ripristina = function () {
      $$("input, select, textarea", form).forEach(function (el) {
        if (!(el.name in s)) return;
        if (el.type === "radio") el.checked = s[el.name] === el.value; else if (el.type === "checkbox") el.checked = !!s[el.name]; else el.value = s[el.name];
      });
    };
    ripristina(); aggiornaMin(params.get("ricompensa") && !s.importo);
    var salva = function () {
      $$("input, select, textarea", form).forEach(function (el) {
        if (el.type === "radio") { if (el.checked) s[el.name] = el.value; } else if (el.type === "checkbox") s[el.name] = el.checked; else s[el.name] = el.value;
      });
      store(KEY, s); riepilogo();
    };
    form.addEventListener("input", salva);
    form.addEventListener("change", function (e) { if (e.target.name === "scelta") { aggiornaMin(true); mostraErrore(importo, ""); } salva(); });
    collegaValidazione(form);

    // riepilogo sempre visibile
    function fee(metodo, x) { var m = D.sito.metodi_pagamento.filter(function (q) { return q.id === metodo; })[0]; return m ? Math.round((x * m.percentuale / 100 + m.fisso) * 100) / 100 : 0; }
    function riepilogo() {
      var r = scelta(), n = numero(importo.value);
      $("[data-sum-progetto]").textContent = p.titolo[LANG];
      $("[data-sum-ricompensa]").textContent = r ? (r.id === "libera" ? G.sum_free : r.titolo) : "—";
      $("[data-sum-importo]").textContent = isNaN(n) ? "—" : euro(n);
      $$("[data-commissione]").forEach(function (el) {
        var f = fee(el.getAttribute("data-commissione"), isNaN(n) ? 0 : n);
        el.textContent = f ? tpl(G.s4_fee, { fee: euro(f) }) : G.s4_fee_none;
      });
    }
    riepilogo();

    // passi
    var sezioni = $$("[data-passo]", form), ind = $$("[data-passo-ind]"), box = $("[data-errori]");
    var passoCorrente = 1;
    function primoIncompleto(fino) {
      for (var i = 1; i < fino; i++) {
        var sez = sezioni[i - 1], h = sez.hidden; sez.hidden = false;
        var ok = $$("input:not([type=radio]), select, textarea", sez).every(function (el) { return !controlla(el); }) &&
          $$("fieldset[data-gruppo]", sez).every(function (fs) { return !controllaGruppo(fs); });
        sez.hidden = h; if (!ok) return i;
      }
      return fino;
    }
    function mostra(n, focus) {
      n = Math.max(1, Math.min(tot, n)); n = primoIncompleto(n); passoCorrente = n;
      sezioni.forEach(function (sz, i) { sz.hidden = i !== n - 1; });
      ind.forEach(function (li, i) {
        li.classList.toggle("is-done", i < n - 1);
        if (i === n - 1) li.setAttribute("aria-current", "step"); else li.removeAttribute("aria-current");
        li.innerHTML = esc(G.steps[i]) + (i < n - 1 ? ' <span class="vh">(' + esc(G.done_step) + ")</span>" : "");
      });
      $("[data-passo-testo]").textContent = tpl(G.step_of, { n: n, tot: tot }) + ": " + G.steps[n - 1];
      box.hidden = true;
      if (n === 5) revisione();
      if (focus) { var h = $("h2", sezioni[n - 1]); h.setAttribute("tabindex", "-1"); h.focus(); }
    }
    function vai(n) {
      var q = new URLSearchParams(location.search); q.set("passo", n);
      history.pushState({ ib: n }, "", location.pathname + "?" + q);
      mostra(n, true);
    }
    window.addEventListener("popstate", function () { mostra(+(new URLSearchParams(location.search).get("passo") || 1), true); });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var errori = validaAmbito(sezioni[passoCorrente - 1]);
      if (errori.length) { riepilogoErrori(box, errori); return; }
      if (passoCorrente < tot) { vai(passoCorrente + 1); return; }
      paga();
    });
    $$("[data-indietro]", form).forEach(function (b) {
      b.addEventListener("click", function () { if (history.state && history.state.ib) history.back(); else { var q = new URLSearchParams(location.search); q.set("passo", passoCorrente - 1); history.replaceState(null, "", location.pathname + "?" + q); mostra(passoCorrente - 1, true); } });
    });
    $("[data-modifica]").addEventListener("click", function (e) { e.preventDefault(); vai(1); });

    function nomeMetodo(id) { var m = D.sito.metodi_pagamento.filter(function (q) { return q.id === id; })[0]; return m ? m.nome[LANG] : "—"; }
    function dati() {
      var r = scelta(), n = numero(importo.value), f = fee(s.metodo, n);
      return { slug: p.slug, titolo: p.titolo[LANG], ricompensa: r.id === "libera" ? G.sum_free : r.titolo, importo: n, fee: f, totale: n + f,
        metodo: nomeMetodo(s.metodo), visibile: s.visibilita === "si", email: (s.email || "").trim(), lang: LANG };
    }
    function righeRiepilogo(d) {
      var r = [[G.r_project, d.titolo], [G.r_reward, d.ricompensa], [G.r_amount, euro(d.importo)], [G.r_fee, d.fee ? euro(d.fee) : I.js.fee_none],
        [G.r_total, euro(d.totale)], [G.r_method, d.metodo], [G.r_visible, d.visibile ? G.r_visible_yes : G.r_visible_no], [G.r_email, d.email]];
      return r.map(function (x, i) { return '<dt' + (i === 4 ? ' class="total"' : "") + ">" + esc(x[0]) + '</dt><dd' + (i === 4 ? ' class="total"' : "") + ">" + esc(x[1]) + "</dd>"; }).join("");
    }
    function revisione() { $("[data-revisione]").innerHTML = righeRiepilogo(dati()); }
    function paga() {
      var btn = $("[data-paga]", form), testo = btn.textContent;
      btn.setAttribute("aria-busy", "true"); btn.disabled = true; btn.textContent = I.js.processing;
      window.setTimeout(function () {
        var d = dati(); d.codice = "IB-" + iso(oggi()).replace(/-/g, "") + "-" + Math.random().toString(36).slice(2, 6).toUpperCase();
        d.righe = righeRiepilogo(d);
        store("ib-ultima-donazione", d); store(KEY, null);
        btn.textContent = testo;
        location.href = "donazione-conferma.html";
      }, 1200);
    }
    var iniziale = +(params.get("passo") || 1);
    history.replaceState({ ib: iniziale }, "", location.href);
    mostra(iniziale, false);
  }

  /* ---------- conferma della donazione ---------- */
  var conf = $("[data-conferma]");
  if (conf && D) {
    var d = store("ib-ultima-donazione");
    if (d) {
      conf.hidden = false; $("[data-conferma-assente]").hidden = true;
      $("[data-codice]").textContent = d.codice;
      $("[data-conferma-riepilogo]").innerHTML = d.righe;
      $("[data-conferma-passi]").innerHTML = I.conferma.next.map(function (x) { return "<li>" + tpl(x, { email: esc(d.email) }) + "</li>"; }).join("");
      $("[data-conferma-progetto]").href = "progetto-" + d.slug + ".html";
      var h = $("h1", conf); h.setAttribute("tabindex", "-1"); h.focus();
    }
  }

  /* ---------- 404: mostra l'indirizzo richiesto ---------- */
  var ind404 = $("[data-indirizzo]");
  if (ind404) {
    var da = new URLSearchParams(location.search).get("da") || (location.protocol !== "file:" && !/404\.html$/.test(location.pathname) ? location.pathname : "");
    if (da) { $("[data-indirizzo-testo]").textContent = da; ind404.hidden = false; }
  }
})();
