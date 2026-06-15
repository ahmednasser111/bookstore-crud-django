document.addEventListener("DOMContentLoaded", () => {

	const deleteButtons = document.querySelectorAll(".btn-danger");
	deleteButtons.forEach((button) => {
		button.addEventListener("click", (e) => {
			if (!confirm("Are you sure you want to proceed?")) {
				e.preventDefault();
			}
		});
	});

	const bookCards = document.querySelectorAll(".book-card");
	bookCards.forEach((card, index) => {
		card.style.opacity = "0";
		card.style.transform = "translateY(20px)";

		setTimeout(() => {
			card.style.transition = "opacity 0.5s ease, transform 0.5s ease";
			card.style.opacity = "1";
			card.style.transform = "translateY(0)";
		}, index * 100);
	});
});
