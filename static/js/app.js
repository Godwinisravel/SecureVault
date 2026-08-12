/* =========================================================
   SecureVault - Global JavaScript
   ========================================================= */

document.addEventListener("DOMContentLoaded", function () {

    /*
     * Automatically focus the first visible form input.
     */
    const firstInput = document.querySelector(
        "main form input:not([type='hidden']):not([disabled])"
    );

    if (firstInput) {
        // Don't steal focus on pages where the user may already
        // be interacting with another element.
        if (!document.activeElement ||
            document.activeElement === document.body) {
            firstInput.focus();
        }
    }

    /*
     * Automatically hide Bootstrap alerts after a few seconds.
     */
    const alerts = document.querySelectorAll(
        ".alert.alert-dismissible"
    );

    alerts.forEach(function (alert) {

        setTimeout(function () {

            if (typeof bootstrap !== "undefined") {
                const bsAlert = bootstrap.Alert.getOrCreateInstance(
                    alert
                );

                bsAlert.close();
            }

        }, 5000);
    });
});


/* =========================================================
   Copy Text Helper
   ========================================================= */

function copyText(text) {

    if (!text) {
        return Promise.reject("Nothing to copy.");
    }

    if (navigator.clipboard &&
        window.isSecureContext) {

        return navigator.clipboard.writeText(text);
    }

    /*
     * Fallback for local development / older browsers.
     */
    const textarea = document.createElement("textarea");

    textarea.value = text;
    textarea.style.position = "fixed";
    textarea.style.left = "-9999px";
    textarea.style.top = "0";

    document.body.appendChild(textarea);

    textarea.focus();
    textarea.select();

    try {
        document.execCommand("copy");
        document.body.removeChild(textarea);

        return Promise.resolve();
    } catch (error) {
        document.body.removeChild(textarea);

        return Promise.reject(error);
    }
}


/* =========================================================
   Copy Button Feedback
   ========================================================= */

function showCopySuccess(button) {

    if (!button) {
        return;
    }

    const icon = button.querySelector("i");

    if (!icon) {
        return;
    }

    const originalClass = icon.className;

    icon.className = "bi bi-check-lg text-success";

    setTimeout(function () {
        icon.className = originalClass;
    }, 2000);
}