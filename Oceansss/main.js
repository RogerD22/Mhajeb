

// Select all organ elements
const organs = document.querySelectorAll('.organ');
const infoBox = document.getElementById('info-box');

// Add hover and click events
organs.forEach(organ => {
  // On mouse enter: show info box
  organ.addEventListener('mouseenter', (e) => {
    const info = e.target.getAttribute('data-info');
    infoBox.textContent = info;
    infoBox.style.display = 'block';
    infoBox.style.top = `${e.pageY - 50}px`;
    infoBox.style.left = `${e.pageX + 20}px`;
  });

  // On mouse leave: hide info box
  organ.addEventListener('mouseleave', () => {
    infoBox.style.display = 'none';
  });
});
