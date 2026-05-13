document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("projects-search");
    const projectCards = document.querySelectorAll(".project-card");

    if (!searchInput || projectCards.length === 0) {
        return;
    }

    searchInput.addEventListener("input", () => {
        // Obtener términos separados por comas
        const terms = searchInput.value
            .toLowerCase()
            .split(",")
            .map(term => term.trim())
            .filter(term => term !== "");

        projectCards.forEach(card => {
            const searchableText = card.dataset.search.toLowerCase();

            // Si no hay términos, mostrar todo
            const matches = terms.length === 0 ||
                terms.every(term => searchableText.includes(term));

            card.style.display = matches ? "block" : "none";
        });
    });
});