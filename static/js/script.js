// Smooth Scrolling for Navigation Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Navbar Scroll Effect
let lastScroll = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll <= 0) {
        navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.1)';
        return;
    }

    if (currentScroll > lastScroll && currentScroll > 100) {
        // Scrolling down
        navbar.style.transform = 'translateY(-100%)';
    } else {
        // Scrolling up
        navbar.style.transform = 'translateY(0)';
        navbar.style.boxShadow = '0 4px 30px rgba(0, 0, 0, 0.15)';
    }

    lastScroll = currentScroll;
});

// Active Navigation Link on Scroll
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-menu a');

window.addEventListener('scroll', () => {
    let current = '';

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;

        if (window.pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Search Functionality
const searchButton = document.querySelector('.btn-search');
const destinationInput = document.getElementById('destination');
const checkinInput = document.getElementById('checkin');
const checkoutInput = document.getElementById('checkout');
const guestsSelect = document.getElementById('guests');

if (searchButton) {
    searchButton.addEventListener('click', () => {
        const destination = destinationInput.value;
        const checkin = checkinInput.value;
        const checkout = checkoutInput.value;
        const guests = guestsSelect.value;

        if (!destination) {
            alert('Please enter a destination!');
            destinationInput.focus();
            return;
        }

        if (!checkin || !checkout) {
            alert('Please select check-in and check-out dates!');
            return;
        }

        // Validate dates
        if (new Date(checkin) >= new Date(checkout)) {
            alert('Check-out date must be after check-in date!');
            return;
        }

        // Show loading animation
        searchButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Searching...';
        searchButton.disabled = true;

        // Simulate search (in real app, this would make an API call)
        setTimeout(() => {
            searchButton.innerHTML = '<i class="fas fa-search"></i> Search';
            searchButton.disabled = false;

            // Scroll to hotels section
            document.querySelector('#hotels').scrollIntoView({ behavior: 'smooth' });

            // Show notification
            showNotification(`Searching for hotels in ${destination}...`, 'success');
        }, 1500);
    });
}

// View Hotel Function
function viewHotel(hotelId) {
    window.location.href = `/hotel/${hotelId}`;
}

    // Add 3D flip animation
    const card = event.target.closest('.hotel-card');
    card.style.transition = 'transform 0.6s';
    card.style.transform = 'perspective(1000px) rotateY(180deg)';

    setTimeout(() => {
        card.style.transform = 'perspective(1000px) rotateY(0deg)';
        // In a real app, this would navigate to hotel details page
        console.log('Viewing hotel:', hotelId);
    }, 600);
}

// Notification System
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }

    // Create notification
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'}"></i>
        <span>${message}</span>
    `;

    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        background: ${type === 'success' ? '#48bb78' : type === 'error' ? '#f56565' : '#667eea'};
        color: white;
        padding: 15px 25px;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        z-index: 10000;
        display: flex;
        align-items: center;
        gap: 10px;
        animation: slideInRight 0.3s ease-out;
    `;

    document.body.appendChild(notification);

    // Auto remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease-out';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Add notification animations to CSS dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Set minimum date for check-in (today)
if (checkinInput) {
    const today = new Date().toISOString().split('T')[0];
    checkinInput.setAttribute('min', today);

    checkinInput.addEventListener('change', () => {
        // Set minimum checkout date to day after checkin
        const checkinDate = new Date(checkinInput.value);
        checkinDate.setDate(checkinDate.getDate() + 1);
        const minCheckout = checkinDate.toISOString().split('T')[0];
        checkoutInput.setAttribute('min', minCheckout);
    });
}

// Parallax Effect for Hero Section
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const parallax = document.querySelector('.hero');

    if (parallax) {
        parallax.style.transform = `translateY(${scrolled * 0.5}px)`;
    }
});

// Hotel Card Hover 3D Effect
const hotelCards = document.querySelectorAll('.hotel-card');

hotelCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = (y - centerY) / 10;
        const rotateY = (centerX - x) / 10;

        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-10px)`;
    });

    card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
    });
});

// Counter Animation for Stats
const statCards = document.querySelectorAll('.stat-card h3');
const observerOptions = {
    threshold: 0.5
};

const animateCounter = (element) => {
    const target = parseInt(element.textContent);
    const duration = 2000;
    const increment = target / (duration / 16);
    let current = 0;

    const updateCounter = () => {
        current += increment;
        if (current < target) {
            element.textContent = Math.floor(current);
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = target;
        }
    };

    updateCounter();
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCounter(entry.target);
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

statCards.forEach(card => observer.observe(card));

// Loading Screen
window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s';
        document.body.style.opacity = '1';
    }, 100);
});

console.log('🏨 LuxStay Hotel Booking System Loaded Successfully!');