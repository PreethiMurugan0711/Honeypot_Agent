document.querySelectorAll("button").forEach(btn => {
  btn.addEventListener("mouseover", () => {
    btn.style.boxShadow = "0 0 10px #00eaff";
  });
  btn.addEventListener("mouseout", () => {
    btn.style.boxShadow = "none";
  });
});
