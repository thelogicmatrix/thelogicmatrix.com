<script>
// Get all gallery images
const images = document.querySelectorAll('.masonry-gallery img');

// Create modal element
const modal = document.createElement('div');
modal.classList.add('modal');
modal.innerHTML = `<span class="modal-close">&times;</span><img src="" alt="Image" />`;
document.body.appendChild(modal);

// Modal close functionality
modal.querySelector('.modal-close').addEventListener('click', () => {
    modal.style.display = 'none';
});

// Open modal when an image is clicked
images.forEach(img => {
    img.addEventListener('click', () => {
        const imgSrc = img.src;
        modal.querySelector('img').src = imgSrc;
        modal.style.display = 'flex'; // Display the modal
    });
});
</script>
