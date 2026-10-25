
document.addEventListener("DOMContentLoaded", () => {

    const navLinks = document.querySelectorAll(
        ".sidebar-nav .nav-link"
    );

    const sections = [...navLinks]
        .map(link => {
            const id = link.getAttribute("href")?.slice(1);
            return document.getElementById(id);
        })
        .filter(Boolean);

    function setActive(id) {
        navLinks.forEach(link => {
            const isActive = link.getAttribute("href") === `#${id}`;

            link.classList.toggle("active", isActive);

            if (isActive) {
                link.setAttribute("aria-current", "location");
            } else {
                link.removeAttribute("aria-current");
            }
        });
    }

    function updateActiveSection() {
        const scrollPosition = window.scrollY + 160;

        let currentSection = sections[0];

        sections.forEach(section => {
            if (section.offsetTop <= scrollPosition) {
                currentSection = section;
            }
        });

        const reachedBottom =
            window.innerHeight + window.scrollY >=
            document.documentElement.scrollHeight - 5;

        if (reachedBottom) {
            currentSection = sections[sections.length - 1];
        }

        if (currentSection) {
            setActive(currentSection.id);
        }
    }

    let ticking = false;

    window.addEventListener("scroll", () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                updateActiveSection();
                ticking = false;
            });
            ticking = true;
        }
    }, { passive: true });

    window.addEventListener("resize", updateActiveSection);

    navLinks.forEach(link => {
        link.addEventListener("click", () => {
            setActive(link.getAttribute("href").slice(1));
        });
    });

    updateActiveSection();
});
