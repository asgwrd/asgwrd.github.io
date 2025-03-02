(function() {
    // Create the overlay element for "Access Denied" message
    let overlay = document.createElement('div');
    overlay.id = 'auth-overlay';
    overlay.style.position = 'fixed';
    overlay.style.top = '0';
    overlay.style.left = '0';
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'white';
    overlay.style.zIndex = '9999';
    overlay.style.display = 'flex';
    overlay.style.justifyContent = 'center';
    overlay.style.alignItems = 'center';
    overlay.innerHTML = '<div style="text-align: center;"><h2>Access Denied</h2><p>Please refresh the page to enter the passcode.</p></div>';
    document.body.appendChild(overlay);

    // Helper function to get a cookie by name
    function getCookie(name) {
        let cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            let [cookieName, cookieValue] = cookie.split('=');
            if (cookieName.trim() === name) {
                return cookieValue;
            }
        }
        return null;
    }

    // Helper function to set a cookie
    function setCookie(name, value) {
        document.cookie = `${name}=${value}; path=/; expires=Fri, 31 Dec 9999 23:59:59 GMT`;
    }

    // Helper function to remove the overlay
    function removeOverlay() {
        let overlay = document.getElementById('auth-overlay');
        if (overlay) {
            overlay.remove();
        }
    }

    // Check if the user is already authenticated via cookie
    if (getCookie('auth') === 'hawktuahaoeneedstobenerfed69420') {
        removeOverlay();
    } else {
        // Prompt for passcode
        let passcode = prompt('Enter the passcode:');
        if (passcode === 'hawktuahaoeneedstobenerfed69420') {  // Replace '1234' with your desired passcode
            setCookie('auth', passcode);
            removeOverlay();
        } else {
            alert('Incorrect passcode');
            // Overlay remains
        }
    }
})();
