// Form validation
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('.needs-validation');
    
    forms.forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
});

// Date input restrictions
const dateInputs = document.querySelectorAll('input[type="date"]');
dateInputs.forEach(input => {
    const today = new Date().toISOString().split('T')[0];
    input.setAttribute('min', today);
});

// Dynamic seat selection
function updatePrice() {
    const seatsSelect = document.getElementById('seats');
    const pricePerSeat = document.getElementById('price-per-seat');
    const totalPrice = document.getElementById('total-price');
    
    if (seatsSelect && pricePerSeat && totalPrice) {
        const seats = parseInt(seatsSelect.value);
        const price = parseFloat(pricePerSeat.dataset.price);
        totalPrice.textContent = (seats * price).toFixed(2);
    }
}

// Search form auto-complete
function initializeAutocomplete() {
    const departureInput = document.getElementById('departure');
    const destinationInput = document.getElementById('destination');
    
    if (departureInput && destinationInput) {
        // Add your preferred autocomplete library implementation here
        // Example: Google Places Autocomplete
    }
}

// Responsive navigation
const navbarToggler = document.querySelector('.navbar-toggler');
const navbarCollapse = document.querySelector('.navbar-collapse');

if (navbarToggler && navbarCollapse) {
    navbarToggler.addEventListener('click', () => {
        navbarCollapse.classList.toggle('show');
    });
}

// Flash messages
function showFlashMessage(message, type = 'info') {
    const flashContainer = document.createElement('div');
    flashContainer.className = `alert alert-${type} alert-dismissible fade show`;
    flashContainer.role = 'alert';
    
    flashContainer.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    document.body.insertBefore(flashContainer, document.body.firstChild);
    
    setTimeout(() => {
        flashContainer.remove();
    }, 5000);
}

// Booking confirmation modal
function showBookingConfirmation(rideId, availableSeats) {
    const modal = document.getElementById('bookingModal');
    if (modal) {
        const seatsInput = modal.querySelector('#seats');
        if (seatsInput) {
            seatsInput.max = availableSeats;
        }
        
        const form = modal.querySelector('form');
        if (form) {
            form.action = `/book-ride/${rideId}`;
        }
        
        const bootstrapModal = new bootstrap.Modal(modal);
        bootstrapModal.show();
    }
}

// Scroll animations
function handleScrollAnimations() {
    const elements = document.querySelectorAll('.animate-on-scroll');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    elements.forEach(element => observer.observe(element));
}

// Ride card interactions
function initializeRideCards() {
    const rideCards = document.querySelectorAll('.ride-card');
    const rideModal = new bootstrap.Modal(document.getElementById('rideModal'));
    
    rideCards.forEach(card => {
        // Quick view interaction
        const quickViewBtn = card.querySelector('.quick-view');
        if (quickViewBtn) {
            quickViewBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                
                // Get ride details
                const carImage = card.querySelector('.car-image img').src;
                const driverAvatar = card.querySelector('.driver-avatar').src;
                const driverName = card.querySelector('h4').textContent;
                const rating = card.querySelector('.rating-count').textContent;
                const carModel = card.querySelector('.text-primary').textContent;
                
                // Update modal content
                document.querySelector('.modal-car-image').src = carImage;
                document.querySelector('.modal-driver-avatar').src = driverAvatar;
                document.querySelector('.modal-driver-name').textContent = driverName;
                document.querySelector('.modal-rating .rating-count').textContent = rating;
                document.querySelector('.modal-car-model').textContent = carModel;
                
                // Show modal
                rideModal.show();
            });
        }
        
        // Hover animations for stats
        const stats = card.querySelectorAll('.driver-stats .number');
        stats.forEach(stat => {
            stat.addEventListener('mouseover', () => {
                stat.style.transform = 'scale(1.1)';
            });
            stat.addEventListener('mouseout', () => {
                stat.style.transform = 'scale(1)';
            });
        });
    });
}

// Time slot selection
function initializeTimeSlots() {
    const timeSlots = document.querySelectorAll('.time-slot');
    const bookRideBtn = document.querySelector('.book-ride-btn');
    
    timeSlots.forEach(slot => {
        slot.addEventListener('click', () => {
            // Remove active class from all slots
            timeSlots.forEach(s => s.classList.remove('active', 'btn-primary'));
            s.classList.add('btn-outline-primary');
            
            // Add active class to selected slot
            slot.classList.add('active');
            slot.classList.remove('btn-outline-primary');
            slot.classList.add('btn-primary');
            
            // Enable book ride button
            bookRideBtn.disabled = false;
        });
    });
}

// Rating hover effect
function initializeRatingHover() {
    const ratings = document.querySelectorAll('.rating');
    
    ratings.forEach(rating => {
        const stars = rating.querySelector('.stars');
        
        rating.addEventListener('mouseover', () => {
            stars.style.transform = 'scale(1.1)';
        });
        
        rating.addEventListener('mouseout', () => {
            stars.style.transform = 'scale(1)';
        });
    });
}

// Loading animation
function showLoadingState() {
    const cards = document.querySelectorAll('.ride-card');
    cards.forEach(card => {
        card.classList.add('loading-shimmer');
    });
}

function hideLoadingState() {
    const cards = document.querySelectorAll('.ride-card');
    cards.forEach(card => {
        card.classList.remove('loading-shimmer');
    });
}

// Initialize all interactions
document.addEventListener('DOMContentLoaded', () => {
    handleScrollAnimations();
    initializeRideCards();
    initializeTimeSlots();
    initializeRatingHover();
    
    // Simulate loading state
    showLoadingState();
    setTimeout(hideLoadingState, 1000);
});
