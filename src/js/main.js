// Main JavaScript entry point
import 'bootstrap';
import { Tooltip, Toast, Popover } from 'bootstrap';
import 'bootstrap-icons/font/bootstrap-icons.css';

// Initialize tooltips
document.addEventListener('DOMContentLoaded', () => {
  // Initialize all tooltips
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(tooltipTriggerEl => new Tooltip(tooltipTriggerEl));

  // Initialize all popovers
  const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
  popoverTriggerList.map(popoverTriggerEl => new Popover(popoverTriggerEl));

  // Toggle password visibility
  document.querySelectorAll('.toggle-password').forEach(button => {
    button.addEventListener('click', function() {
      const input = this.previousElementSibling;
      const type = input.getAttribute('type') === 'password' ? 'text' : 'password';
      input.setAttribute('type', type);
      this.querySelector('i').classList.toggle('bi-eye');
      this.querySelector('i').classList.toggle('bi-eye-slash');
    });
  });

  // Form validation
  const forms = document.querySelectorAll('.needs-validation');
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add('was-validated');
    }, false);
  });

  // Auto-hide alerts after 5 seconds
  const alerts = document.querySelectorAll('.alert-dismissible');
  alerts.forEach(alert => {
    setTimeout(() => {
      const bsAlert = new bootstrap.Alert(alert);
      bsAlert.close();
    }, 5000);
  });
});

// Export for use in other modules
window.bootstrap = { Tooltip, Toast, Popover };

// Add CSRF token to all AJAX requests
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
if (csrftoken) {
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });
}

// Add a simple fetch wrapper for API calls
window.api = {
  get: (url, options = {}) => fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'X-Requested-With': 'XMLHttpRequest',
      ...options.headers
    },
    ...options
  }),
  
  post: (url, data = {}, options = {}) => fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': csrftoken,
      ...options.headers
    },
    body: JSON.stringify(data),
    ...options
  }),
  
  put: (url, data = {}, options = {}) => fetch(url, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': csrftoken,
      ...options.headers
    },
    body: JSON.stringify(data),
    ...options
  }),
  
  delete: (url, options = {}) => fetch(url, {
    method: 'DELETE',
    headers: {
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': csrftoken,
      ...options.headers
    },
    ...options
  })
};

// Add utility functions
window.utils = {
  debounce: (func, wait) => {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  },
  
  throttle: (func, limit) => {
    let inThrottle;
    return function executedFunction(...args) {
      if (!inThrottle) {
        func(...args);
        inThrottle = true;
        setTimeout(() => inThrottle = false, limit);
      }
    };
  },
  
  formatDate: (dateString) => {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
  },
  
  formatCurrency: (amount, currency = 'USD') => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: currency
    }).format(amount);
  },
  
  copyToClipboard: (text) => {
    return navigator.clipboard.writeText(text);
  }
};

// Initialize any page-specific JavaScript
if (document.body.dataset.page) {
  import(`./pages/${document.body.dataset.page}.js`)
    .catch(err => console.log(`No page script found for ${document.body.dataset.page}`));
}
