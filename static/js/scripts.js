document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('contactSearch');
    const tableRows = document.querySelectorAll('tbody tr');

    if (searchInput) {
        searchInput.addEventListener('keyup', function(e) {
            const term = e.target.value.toLowerCase();
            
            tableRows.forEach(row => {
                const name = row.cells[0].textContent.toLowerCase();
                const email = row.cells[1].textContent.toLowerCase();
                
                if (name.includes(term) || email.includes(term)) {
                    row.style.display = "";
                } else {
                    row.style.display = "none";
                }
            });
        });
    }

    const modal = document.getElementById('contactModal');
    const modalClose = document.getElementById('modalClose');
    const viewButtons = document.querySelectorAll('.view-contact');
    const modalName = document.getElementById('modalName');
    const modalEmail = document.getElementById('modalEmail');
    const modalPhone = document.getElementById('modalPhone');
    const modalCategory = document.getElementById('modalCategory');
    const modalEdit = document.getElementById('modalEdit');
    const modalDeleteForm = document.getElementById('modalDeleteForm');

    function showModal(contactRow) {
        const pk = contactRow.dataset.pk;
        const firstName = contactRow.dataset.firstName;
        const lastName = contactRow.dataset.lastName;
        const email = contactRow.dataset.email;
        const phone = contactRow.dataset.phone;
        const category = contactRow.dataset.category;
        const imageUrl = contactRow.dataset.imageUrl;

        modalName.textContent = `${firstName} ${lastName}`;
        modalEmail.textContent = email;
        modalPhone.textContent = phone;
        modalCategory.textContent = category;

        if (imageUrl) {
            document.getElementById('modalImage').src = imageUrl;
            document.getElementById('modalImage').style.display = 'block';
            document.getElementById('modalImagePlaceholder').style.display = 'none';
        } else {
            document.getElementById('modalImage').style.display = 'none';
            document.getElementById('modalImagePlaceholder').style.display = 'block';
            const initials = `${firstName[0] || ''}${lastName[0] || ''}`.toUpperCase();
            document.getElementById('modalImagePlaceholder').textContent = initials;
        }

        modalEdit.href = `/contact/${pk}/edit/`;
        modalDeleteForm.action = `/contact/${pk}/delete/`;

        modal.style.display = 'flex';
    }

    function hideModal() {
        modal.style.display = 'none';
    }

    viewButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.stopPropagation();
            const row = button.closest('.contact-row');
            showModal(row);
        });
    });

    modalClose.addEventListener('click', function() {
        hideModal();
    });

    const modalChangeImage = document.getElementById('modalChangeImage');

    modalChangeImage.addEventListener('click', function(e) {
        e.preventDefault();
        const pk = modalDeleteForm.action.match(/contact\/(\d+)\/delete\//);
        if (pk && pk[1]) {
            window.location.href = `/contact/${pk[1]}/edit/`;
        }
    });

    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            hideModal();
        }
    });

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.style.display === 'flex') {
            hideModal();
        }
    });
});