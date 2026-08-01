---
icon: fas fa-file-lines
order: 2
title: CV
---

<div class="cv-doc">

<style>
/* ====================================================================
   Página de CV — expediente técnico.

   Misma pareja tipográfica que el CV impreso (serif Palatino para la
   prosa, monoespaciada para los metadatos) para que el PDF y la web se
   lean como un mismo sistema. Aquí no hay ATS, así que sí hay color,
   profundidad y movimiento.

   Todo va prefijado con .cv-doc para no contaminar el tema Chirpy.
   ==================================================================== */

.cv-doc {
  --tinta: #e8e4dc;
  --tinta-2: #a49e93;
  --tinta-3: #6f6a62;
  --fondo: #16161a;
  --fondo-2: #1c1c21;
  --acento: #d9954f;
  --acento-2: #8fb8c9;
  --linea: #2e2e35;

  --serif: "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif;
  --mono: ui-monospace, "Cascadia Code", "JetBrains Mono", Consolas, monospace;

  background: var(--fondo);
  color: var(--tinta);
  font-family: var(--serif);
  border: 1px solid var(--linea);
  border-radius: 3px;
  padding: 0;
  margin: 0 0 2rem;
  overflow: hidden;
  position: relative;
}

/* ---------- cabecera ---------- */

.cv-doc .hero {
  position: relative;
  padding: 3.2rem 2.4rem 2.2rem;
  border-bottom: 1px solid var(--linea);
  background:
    radial-gradient(120% 140% at 12% -20%, rgba(217,149,79,.14), transparent 58%),
    linear-gradient(180deg, var(--fondo-2), var(--fondo));
  overflow: hidden;
}

/* Retícula tenue de fondo: textura, no decoración evidente. */
.cv-doc .hero::before {
  content: "";
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(var(--linea) 1px, transparent 1px),
    linear-gradient(90deg, var(--linea) 1px, transparent 1px);
  background-size: 34px 34px;
  opacity: .35;
  mask-image: radial-gradient(90% 80% at 70% 0%, #000, transparent 75%);
  pointer-events: none;
}

.cv-doc .hero > * { position: relative; }

.cv-doc .nombre {
  font-family: var(--serif);
  font-size: clamp(2.1rem, 6vw, 3.4rem);
  line-height: 1.02;
  margin: 0;
  font-weight: 700;
  letter-spacing: -0.5px;
}

.cv-doc .nombre::after {
  content: "";
  display: block;
  width: 62px;
  height: 3px;
  margin-top: 1rem;
  background: var(--acento);
}

.cv-doc .rol {
  font-family: var(--mono);
  font-size: .74rem;
  text-transform: uppercase;
  letter-spacing: .18em;
  color: var(--acento);
  margin: 1rem 0 0;
}

.cv-doc .prompt {
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--tinta-2);
  margin-top: 1.4rem;
  line-height: 1.9;
}
.cv-doc .prompt .sig { color: var(--acento-2); }
.cv-doc .prompt .caret {
  display: inline-block;
  width: .5em;
  height: 1em;
  background: var(--acento);
  vertical-align: -.15em;
  animation: cvCaret 1.15s steps(1) infinite;
}
@keyframes cvCaret { 0%,50% { opacity: 1 } 50.01%,100% { opacity: 0 } }

.cv-doc .acciones { margin-top: 1.8rem; display: flex; flex-wrap: wrap; gap: .7rem; }

.cv-doc .btn {
  font-family: var(--mono);
  font-size: .74rem;
  letter-spacing: .07em;
  text-transform: uppercase;
  text-decoration: none;
  padding: .62rem 1.1rem;
  border: 1px solid var(--linea);
  color: var(--tinta-2);
  background: transparent;
  transition: color .18s, border-color .18s, background .18s, transform .18s;
}
.cv-doc .btn:hover {
  color: var(--fondo);
  background: var(--acento);
  border-color: var(--acento);
  transform: translateY(-1px);
}
.cv-doc .btn.primario {
  color: var(--acento);
  border-color: var(--acento);
}
.cv-doc .btn.primario:hover { color: var(--fondo); }

/* ---------- cuerpo ---------- */

.cv-doc .cuerpo { padding: 2.2rem 2.4rem 2.6rem; }

.cv-doc section { margin-bottom: 2.5rem; }
.cv-doc section:last-child { margin-bottom: 0; }

.cv-doc h2 {
  font-family: var(--mono);
  font-size: .7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .2em;
  color: var(--tinta-3);
  margin: 0 0 1.2rem;
  padding: 0;
  border: 0;
  display: flex;
  align-items: center;
  gap: .9rem;
}
.cv-doc h2::after {
  content: "";
  flex: 1;
  height: 1px;
  background: var(--linea);
}

.cv-doc p { margin: 0 0 .8rem; line-height: 1.72; color: var(--tinta); }
.cv-doc .destacado { color: var(--acento); font-weight: 700; }

/* ---------- entradas numeradas ---------- */

.cv-doc .entrada {
  display: grid;
  grid-template-columns: 3rem 1fr;
  gap: 0 1.2rem;
  padding: 1.1rem 0 1.1rem 0;
  border-top: 1px solid var(--linea);
  position: relative;
}
.cv-doc .entrada::before {
  content: "";
  position: absolute;
  left: -2.4rem;
  top: -1px;
  width: 3px;
  height: calc(100% + 1px);
  background: var(--acento);
  transform: scaleY(0);
  transform-origin: top;
  transition: transform .25s ease;
}
.cv-doc .entrada:hover::before { transform: scaleY(1); }

.cv-doc .num {
  font-family: var(--mono);
  font-size: .82rem;
  color: var(--tinta-3);
  padding-top: .25rem;
  letter-spacing: .04em;
}

.cv-doc .entrada h3 {
  margin: 0;
  font-family: var(--serif);
  font-size: 1.06rem;
  font-weight: 700;
  line-height: 1.35;
  color: var(--tinta);
}

.cv-doc .fecha {
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--tinta-3);
  letter-spacing: .05em;
  margin-top: .25rem;
  display: block;
}

.cv-doc .entrada ul { margin: .7rem 0 0; padding: 0; list-style: none; }
.cv-doc .entrada li {
  position: relative;
  padding-left: 1.1rem;
  margin-bottom: .4rem;
  line-height: 1.65;
  color: var(--tinta-2);
}
.cv-doc .entrada li::before {
  content: "—";
  position: absolute;
  left: 0;
  color: var(--tinta-3);
}

.cv-doc .cred {
  font-family: var(--mono);
  font-size: .68rem;
  color: var(--tinta-3);
  letter-spacing: .03em;
}

/* ---------- filas etiquetadas ---------- */

.cv-doc .fila {
  display: grid;
  grid-template-columns: 8.5rem 1fr;
  gap: .4rem 1.2rem;
  padding: .55rem 0;
  border-top: 1px solid var(--linea);
  align-items: baseline;
}
.cv-doc .fila:last-child { border-bottom: 1px solid var(--linea); }
.cv-doc .etq {
  font-family: var(--mono);
  font-size: .68rem;
  text-transform: uppercase;
  letter-spacing: .13em;
  color: var(--acento-2);
}
.cv-doc .val { color: var(--tinta-2); line-height: 1.6; }

/* ---------- chips de cursos ---------- */

.cv-doc .chips { display: flex; flex-wrap: wrap; gap: .4rem; margin-top: .2rem; }
.cv-doc .chip {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .02em;
  padding: .28rem .6rem;
  border: 1px solid var(--linea);
  color: var(--tinta-2);
  background: var(--fondo-2);
  transition: border-color .18s, color .18s;
}
.cv-doc .chip:hover { border-color: var(--acento); color: var(--tinta); }

/* ---------- entrada escalonada ---------- */

/* El estado inicial vive dentro de los keyframes y no en la regla base:
   así, si el navegador no ejecuta la animación, el contenido sigue
   siendo visible en lugar de quedarse en opacity 0 para siempre. */
@media (prefers-reduced-motion: no-preference) {
  .cv-doc .anim {
    animation: cvEntra .6s cubic-bezier(.22,.61,.36,1) both;
  }
  .cv-doc .anim:nth-child(1) { animation-delay: .04s }
  .cv-doc .anim:nth-child(2) { animation-delay: .10s }
  .cv-doc .anim:nth-child(3) { animation-delay: .16s }
  .cv-doc .anim:nth-child(4) { animation-delay: .22s }
  .cv-doc .anim:nth-child(5) { animation-delay: .28s }
  .cv-doc .anim:nth-child(6) { animation-delay: .34s }
  @keyframes cvEntra {
    from { opacity: 0; transform: translateY(10px) }
    to   { opacity: 1; transform: none }
  }
}

/* ---------- móvil ---------- */

@media (max-width: 640px) {
  .cv-doc .hero { padding: 2.2rem 1.3rem 1.7rem; }
  .cv-doc .cuerpo { padding: 1.6rem 1.3rem 2rem; }
  .cv-doc .entrada { grid-template-columns: 1fr; gap: 0; }
  .cv-doc .num { display: none; }
  .cv-doc .fila { grid-template-columns: 1fr; gap: .15rem; }
  .cv-doc .entrada::before { left: -1.3rem; }
}
</style>

<div class="hero">
  <h1 class="nombre">Marco Rodríguez Fernández</h1>
  <p class="rol">Analista de Ciberseguridad Junior · SOC · Pentesting</p>
  <div class="prompt">
    <span class="sig">objetivo</span> &nbsp;analista SOC nivel 1<br>
    <span class="sig">ubicación</span>&nbsp;Gijón, Asturias · traslado nacional · remoto<br>
    <span class="sig">turnos</span> &nbsp;&nbsp;&nbsp;rotativos 24x7 — prefiero noches<span class="caret"></span>
  </div>
  <div class="acciones">
    <a class="btn primario" href="/assets/cv/CV-Marco-Rodriguez-Fernandez.pdf">Descargar PDF</a>
    <a class="btn" href="mailto:marcurf86@gmail.com">Escríbeme</a>
    <a class="btn" href="https://github.com/marcorfsec">GitHub</a>
    <a class="btn" href="/formacion/">Certificados</a>
  </div>
</div>

<div class="cuerpo">

<section class="anim">
  <h2>Perfil</h2>
  <p>
    Perfil técnico autodidacta con formación intensiva y reciente en seguridad
    ofensiva: 269 laboratorios de hacking web sobre 31 vulnerabilidades reales,
    además de fundamentos de Linux, redes y programación. Preparando la
    certificación eJPT.
  </p>
  <p>
    Busco incorporarme a un SOC de nivel 1 para desarrollar carrera en
    operaciones de seguridad. <span class="destacado">Disponibilidad total para
    turnos rotativos 24x7, incluidas noches, con preferencia por el turno
    nocturno.</span>
  </p>
</section>

<section class="anim">
  <h2>Certificaciones</h2>
  <div class="fila">
    <div class="etq">eJPT</div>
    <div class="val">INE Security — en preparación, examen previsto para septiembre de 2026.</div>
  </div>
</section>

<section class="anim">
  <h2>Proyectos y laboratorios</h2>

  <div class="entrada">
    <div class="num">01</div>
    <div>
      <h3>Explotación de vulnerabilidades web — 269 laboratorios</h3>
      <span class="fecha">julio 2026</span>
      <ul>
        <li>Explotación práctica de 31 clases de vulnerabilidad sobre entornos controlados: inyección SQL, XSS, SSRF, XXE, deserialización insegura, LFI/RFI y fallos de control de acceso.</li>
        <li>Burp Suite para interceptar, modificar y reproducir peticiones; explotación manual antes que automatizada para entender la causa raíz.</li>
        <li><span class="cred">Certificado verificable · ID 5294-9832-3588-2758</span></li>
      </ul>
    </div>
  </div>

  <div class="entrada">
    <div class="num">02</div>
    <div>
      <h3>Enumeración y explotación de sistemas — 53 h</h3>
      <span class="fecha">julio 2026</span>
      <ul>
        <li>Ciclo completo de intrusión sobre máquinas vulnerables: reconocimiento, enumeración de servicios, explotación, acceso y escalada de privilegios en Linux y Windows.</li>
        <li>Nmap, Gobuster, Hydra, Netcat, Metasploit y John the Ripper.</li>
        <li><span class="cred">Certificado verificable · ID 2676-5668-8596-9026</span></li>
      </ul>
    </div>
  </div>

  <div class="entrada">
    <div class="num">03</div>
    <div>
      <h3>Herramientas ofensivas propias en Python — 35 h</h3>
      <span class="fecha">junio 2026</span>
      <ul>
        <li>Desarrollo de utilidades de reconocimiento y automatización: escaneo de puertos con sockets, fuerza bruta de directorios y manipulación de peticiones HTTP.</li>
        <li><span class="cred">Certificado verificable · ID 7909-6445-4078-7259</span></li>
      </ul>
    </div>
  </div>

  <div class="entrada">
    <div class="num">04</div>
    <div>
      <h3>Writeups técnicos</h3>
      <span class="fecha">desde agosto 2026</span>
      <ul>
        <li>Publicación continua de resoluciones de máquinas retiradas de HackTheBox y salas de TryHackMe, documentando la metodología y el razonamiento, no solo el resultado.</li>
      </ul>
    </div>
  </div>
</section>

<section class="anim">
  <h2>Competencias técnicas</h2>
  <div class="fila"><div class="etq">Sistemas</div><div class="val">Linux (Arch, Debian/Kali), administración, permisos, bash, systemd · Windows</div></div>
  <div class="fila"><div class="etq">Redes</div><div class="val">TCP/IP, modelo OSI, DNS, HTTP/HTTPS, análisis de tráfico</div></div>
  <div class="fila"><div class="etq">Ofensiva</div><div class="val">Enumeración, explotación web, escalada de privilegios, post-explotación</div></div>
  <div class="fila"><div class="etq">Herramientas</div><div class="val">Nmap, Burp Suite, Metasploit, Wireshark, Gobuster, Hydra, John the Ripper</div></div>
  <div class="fila"><div class="etq">Lenguajes</div><div class="val">Python, Bash, JavaScript, SQL</div></div>
</section>

<section class="anim">
  <h2>Formación</h2>
  <div class="fila">
    <div class="etq">Hack4u 2026</div>
    <div class="val">
      <div class="chips">
        <span class="chip">Hacking Web</span>
        <span class="chip">Introducción al Hacking · 53 h</span>
        <span class="chip">Python Ofensivo · 35 h</span>
        <span class="chip">Introducción a Linux</span>
        <span class="chip">Entorno en Linux</span>
        <span class="chip">Arch Linux</span>
      </div>
    </div>
  </div>
  <div class="fila">
    <div class="etq">Cisco 2026</div>
    <div class="val">
      <div class="chips">
        <span class="chip">Linux Essentials</span>
        <span class="chip">NDG Linux I</span>
        <span class="chip">NDG Linux II</span>
        <span class="chip">Python Essentials 1</span>
        <span class="chip">Python Essentials 2</span>
        <span class="chip">JavaScript Essentials 1</span>
      </div>
    </div>
  </div>
</section>

<section class="anim">
  <h2>Idiomas</h2>
  <div class="fila"><div class="etq">Español</div><div class="val">Nativo</div></div>
  <div class="fila"><div class="etq">Inglés</div><div class="val">B1 — documentación técnica con soltura; en progresión hacia B2</div></div>
</section>

</div>
</div>
