/* home_page */
function toggleTable(event) {
        if (event) event.stopPropagation();
        const matchCard = document.getElementById('matchCard');
        const tableCard = document.getElementById('tableCard');
        
        if (matchCard.style.opacity === '0') {
            matchCard.style.opacity = '1';
            matchCard.style.pointerEvents = 'auto';
            matchCard.style.transform = 'translateY(0)';
            tableCard.style.opacity = '0';
            tableCard.style.pointerEvents = 'none';
            tableCard.style.transform = 'translateY(1rem)';
        } else {
            matchCard.style.opacity = '0';
            matchCard.style.pointerEvents = 'none';
            matchCard.style.transform = 'translateY(-1rem)';
            tableCard.style.opacity = '1';
            tableCard.style.pointerEvents = 'auto';
            tableCard.style.transform = 'translateY(0)';
        }
    }

    document.addEventListener('DOMContentLoaded', () => {
        const observerOptions = {
            threshold: 0.1
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('opacity-100', 'translate-y-0');
                    entry.target.classList.remove('opacity-0', 'translate-y-10');
                }
            });
        }, observerOptions);

        document.querySelectorAll('.glass-panel').forEach(panel => {
            panel.classList.add('transition-all', 'duration-700', 'ease-out');
        });
    });

/* stadium */

// Interactive Map Logic
        const stadiumPaths = document.querySelectorAll('.stadium-path');
        const tooltip = document.getElementById('map-tooltip');
        const tooltipTitle = document.getElementById('tooltip-title');
        const tooltipDesc = document.getElementById('tooltip-desc');

        stadiumPaths.forEach(path => {
            path.addEventListener('mousemove', (e) => {
                const name = path.getAttribute('data-name');
                const info = path.getAttribute('data-info');
                
                tooltipTitle.innerText = name;
                tooltipDesc.innerText = info;
                
                tooltip.style.left = (e.clientX + 15) + 'px';
                tooltip.style.top = (e.clientY + 15) + 'px';
                tooltip.classList.remove('hidden');
                
                // Active glow effect
                path.style.filter = "drop-shadow(0 0 15px rgba(192, 0, 31, 0.4))";
            });

            path.addEventListener('mouseleave', () => {
                tooltip.classList.add('hidden');
                path.style.filter = "none";
            });
        });

        // Simple Parallax for Hero
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const heroImg = document.querySelector('section img');
            if(heroImg) {
                heroImg.style.transform = `translateY(${scrolled * 0.4}px)`;
            }
        });

/* the team */
// Simple filter logic for demonstration
    const filterButtons = document.querySelectorAll('button.rounded-full');
    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => {
                b.classList.remove('active-filter');
                b.classList.add('bg-white', 'text-on-surface-variant');
            });
            btn.classList.add('active-filter');
            btn.classList.remove('bg-white', 'text-on-surface-variant');
        });
    });

