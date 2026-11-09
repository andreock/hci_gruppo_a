() => { const t = document.body.innerText.replace(/\n{2,}/g, '\n'); const a = t.indexOf('These checks highlight'); const b = t.indexOf('\nBest Practices\n', a); const s = t.slice(a, b);
const g = (re) => { const m = s.match(re); return m ? parseInt(m[1]) : null; };
const pre = t.slice(0, a).trim().split('\n');
return { url: (t.match(/Lighthouse Result (\S+)/) || [null, document.title])[1], lh: (t.match(/Lighthouse \d+\.\d+\.\d+/) || [null])[0], score: parseInt(pre[pre.length - 2]), manual: g(/TO MANUALLY CHECK \((\d+)\)/), passed: g(/PASSED AUDITS \((\d+)\)/), na: g(/NOT APPLICABLE \((\d+)\)/), prima_dei_manuali: s.slice(s.indexOf('encouraged.') + 11, s.indexOf('ADDITIONAL ITEMS')).trim() }; }
