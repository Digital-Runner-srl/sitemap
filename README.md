# sitemap.digitalrunner.it

Copia della sitemap di [digitalrunner.it](https://digitalrunner.it/sitemap.xml), pubblicata con GitHub Pages.

Il sito è su Vercel e da maggio 2026 Google Search Console non riesce a leggere le sitemap servite
da Vercel ([discussione](https://community.vercel.com/t/gsc-cannot-read-any-sitemap-served-from-vercel-cross-host-experiment-isolates-the-platform/48266)).
Il robots.txt del sito indica questa copia: `https://sitemap.digitalrunner.it/sitemap.xml`.

- Ogni ora l'azione *Aggiorna la sitemap* la riscarica e, se è cambiata ed è valida, la salva qui.
  Si può lanciare anche a mano da Actions → Aggiorna la sitemap → Run workflow.
- DNS (Hostinger): `CNAME sitemap → digital-runner-srl.github.io`.
- La sitemap originale la genera `scripts/flat-sitemap.mjs` nel repo del sito: qui non si modifica a mano.
- `test.xml` è una sitemap di controllo (5 URL), fissa e non toccata dall'azione: serve solo a distinguere
  "Google non ha ancora letto questo host" da "Google ha un problema con quel file". Va tolta dopo la prova.
