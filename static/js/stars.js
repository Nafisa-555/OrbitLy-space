(function () {
  const canvas = document.createElement("canvas");
  const ctx    = canvas.getContext("2d");
  const field  = document.getElementById("starfield");

  if (!field) return;

  field.appendChild(canvas);

  Object.assign(canvas.style, {
    position: "absolute", inset: "0",
    width: "100%", height: "100%",
    pointerEvents: "none",
  });

  const STAR_COUNT  = 220;
  const TWINKLE_SPD = 0.008;

  let W, H, stars = [];

  function resize() {
    W = canvas.width  = field.offsetWidth  || window.innerWidth;
    H = canvas.height = field.offsetHeight || window.innerHeight;
  }

  function createStars() {
    stars = [];
    for (let i = 0; i < STAR_COUNT; i++) {
      stars.push({
        x:      Math.random() * W,
        y:      Math.random() * H,
        r:      Math.random() * 1.5 + 0.3,
        alpha:  Math.random(),
        dAlpha: (Math.random() * 0.5 + 0.5) * TWINKLE_SPD * (Math.random() < 0.5 ? 1 : -1),
      });
    }
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);
    for (const s of stars) {
      s.alpha += s.dAlpha;
      if (s.alpha >= 1 || s.alpha <= 0) s.dAlpha *= -1;
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(180, 210, 255, ${Math.max(0, Math.min(1, s.alpha))})`;
      ctx.fill();
    }
    requestAnimationFrame(draw);
  }

  window.addEventListener("resize", () => { resize(); createStars(); });

  resize();
  createStars();
  draw();
})();
