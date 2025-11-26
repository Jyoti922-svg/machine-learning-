// Main JavaScript for handling form submission and API calls

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    const resultContainer = document.getElementById('resultContainer');
    const errorContainer = document.getElementById('errorContainer');
    const submitBtn = form.querySelector('button[type="submit"]');
    const submitText = document.getElementById('submitText');
    const loadingText = document.getElementById('loadingText');

    // Structure information mapping
    const structureInfo = {
        'Honeycomb': 'Honeycomb structures provide excellent strength-to-weight ratio with hexagonal cells. Ideal for applications requiring high stiffness and energy absorption.',
        'Lattice': 'Lattice structures offer uniform load distribution with interconnected struts. Best for lightweight applications with moderate strength requirements.',
        'Voronoi': 'Voronoi structures mimic natural cellular patterns, providing good mechanical properties and aesthetic appeal. Suitable for complex geometries.',
        'Gyroid': 'Gyroid structures feature triply periodic minimal surfaces, offering excellent mechanical properties and efficient material distribution.'
    };

    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        // Hide previous results and errors
        resultContainer.classList.add('hidden');
        errorContainer.classList.add('hidden');

        // Get form values
        const stiffness = parseInt(document.getElementById('stiffness').value);
        const density = parseInt(document.getElementById('density').value);
        const material = document.getElementById('material').value;

        // Validate inputs
        if (!stiffness || !density || !material) {
            showError('Please fill in all fields');
            return;
        }

        if (stiffness < 10 || stiffness > 100) {
            showError('Stiffness must be between 10 and 100');
            return;
        }

        if (density < 5 || density > 50) {
            showError('Density must be between 5 and 50');
            return;
        }

        // Show loading state
        submitBtn.disabled = true;
        submitText.classList.add('hidden');
        loadingText.classList.remove('hidden');

        try {
            // Make API call
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    stiffness: stiffness,
                    density: density,
                    material: material
                })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Prediction failed');
            }

            // Display result
            displayResult(data.recommended_structure, data.confidence);

        } catch (error) {
            console.error('Error:', error);
            showError(error.message || 'An error occurred while making the prediction');
        } finally {
            // Reset button state
            submitBtn.disabled = false;
            submitText.classList.remove('hidden');
            loadingText.classList.add('hidden');
        }
    });

    function displayResult(structure, confidence) {
        const structureName = document.getElementById('structureName');
        const confidenceValue = document.getElementById('confidenceValue');
        const structureInfoElement = document.getElementById('structureInfo');

        structureName.textContent = structure;
        confidenceValue.textContent = (confidence * 100).toFixed(0) + '%';
        structureInfoElement.textContent = structureInfo[structure] || '';

        resultContainer.classList.remove('hidden');

        // Scroll to result
        resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function showError(message) {
        const errorMessage = document.getElementById('errorMessage');
        errorMessage.textContent = message;
        errorContainer.classList.remove('hidden');

        // Scroll to error
        errorContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
});

