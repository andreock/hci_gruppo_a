#!/usr/bin/env python3
"""Confronto «prima / dopo» del re-design.
Ricostruisce in una cartella temporanea la versione provata dagli utenti (branch assignment3), poi sulle due versioni:
  1. esegue il percorso più breve dei 4 task (pilota.js): devono restare completabili prima e dopo;
  2. misura gli aspetti legati ai problemi P1–P8 e salva le schermate (prima_dopo.js).
Scrive dati/misure.json e relazione/img/p*-prima.png, p*-dopo.png, t*.png.
Uso (da assignment4):  python3 relazione/tools/prima_dopo.py [--ref assignment3]"""
import argparse, os, subprocess, sys, tempfile
QUI = os.path.dirname(os.path.abspath(__file__)); REL = os.path.dirname(QUI); A4 = os.path.dirname(REL); REPO = os.path.dirname(A4)
SITO = os.path.join(REPO, "assignment2", "website")

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--ref", default="assignment3", help="branch o commit della versione provata dagli utenti")
    a = ap.parse_args()
    with tempfile.TemporaryDirectory(prefix="ideablume-prima-") as tmp:
        arch = subprocess.run(["git", "-C", REPO, "archive", a.ref, "assignment2/website"], check=True, capture_output=True).stdout
        subprocess.run(["tar", "-x", "-C", tmp], input=arch, check=True)
        prima = os.path.join(tmp, "assignment2", "website")
        for sito in (prima, SITO):  # stessa data di riferimento per le due versioni
            subprocess.run([sys.executable, os.path.join(sito, "tools", "build.py")], check=True, capture_output=True)
        print("== Percorsi dei task sulla versione provata (prima)")
        subprocess.run(["node", os.path.join(QUI, "pilota.js"), prima], check=True)
        print("== Percorsi dei task sulla versione ridisegnata (dopo)")
        subprocess.run(["node", os.path.join(QUI, "pilota.js"), SITO, "--senza-schermate"], check=True)
        print("== Misure e schermate prima/dopo")
        subprocess.run(["node", os.path.join(QUI, "prima_dopo.js"), prima, SITO, os.path.join(REL, "img"), os.path.join(A4, "dati", "misure.json")], check=True)

if __name__ == "__main__":
    main()
