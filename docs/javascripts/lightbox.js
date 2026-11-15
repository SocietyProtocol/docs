// Initialize GLightbox for image zoom
function initLightbox() {
  if (typeof GLightbox === "undefined") return;

  // Find images inside content area
  const images = document.querySelectorAll(".md-content img:not(.no-lightbox)");
  images.forEach((img) => {
    // Avoid double wrapping
    if (img.parentElement.tagName.toLowerCase() === "a") {
      img.parentElement.classList.add("glightbox");
      return;
    }

    const anchor = document.createElement("a");
    anchor.href = img.src;
    anchor.classList.add("glightbox");
    img.parentNode.insertBefore(anchor, img);
    anchor.appendChild(img);
  });

  GLightbox({
    selector: ".glightbox",
    touchNavigation: true,
    loop: true,
    zoomable: true,
    openEffect: "zoom",
    closeEffect: "zoom"
  });
}

document.addEventListener("DOMContentLoaded", initLightbox);

// Support Material for MkDocs instant loading
if (typeof document$ !== "undefined") {
  document$.subscribe(function () {
    initLightbox();
  });
}
