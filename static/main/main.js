window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 10 || document.documentElement.scrollTop > 10) {
    document.getElementById("top-banner").style.display = "none";
    document.getElementById("navbar").style.marginTop = "0";
  } else {
    document.getElementById("top-banner").style.display = "flex";
    document.getElementById("navbar").style.marginTop = "30px";
  }
}
