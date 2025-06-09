document.addEventListener('DOMContentLoaded', function () {
    const dropArea = document.getElementById('drop-area');
    const fileInput = document.getElementById('file-input');
    const fileName = document.getElementById('file-name');
    const submitBtn = document.getElementById('submit-btn');
    const resultCard = document.getElementById('result-card');

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false);
        document.body.addEventListener(eventName, preventDefaults, false);
    });

    ['dragenter', 'dragover'].forEach(eventName => {
        dropArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight, false);
    });

    dropArea.addEventListener('drop', handleDrop, false);

    fileInput.addEventListener('change', handleFiles);

    dropArea.addEventListener('click', function (event) {
        if (!event.target.closest('button')) {
            fileInput.click();
        }
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    function highlight() {
        dropArea.classList.add('highlight');
    }

    function unhighlight() {
        dropArea.classList.remove('highlight');
    }

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;

        if (files && files.length) {
            fileInput.files = files;
            handleFiles();
        }
    }

    function handleFiles() {
        const files = fileInput.files;

        if (files && files.length) {
            updateFileInfo(files[0]);
            submitBtn.disabled = false;
        }
    }

    function updateFileInfo(file) {
        fileName.textContent = file.name;
    }
});