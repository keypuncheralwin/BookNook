const head = document.getElementById("head");

if (head) {
  const goBackBtn = document.getElementById("go-back-btn");
  goBackBtn?.addEventListener("click", () => {
    history.back();
  });
}
