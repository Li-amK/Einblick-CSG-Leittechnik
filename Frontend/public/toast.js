function showToast(message) {
    const toastContainer = document.getElementById('toast-container');
  
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerText = message;
  
    toastContainer.appendChild(toast);
  
    toast.style.display = 'block';
  
    setTimeout(() => {
      toast.style.display = 'none';
      toast.remove();
    }, 6000);
  }
  
 
function handleLoginFormSubmit(event) {
    event.preventDefault();
  
    const formData = new FormData(event.target);
    const urlEncodedData = new URLSearchParams(formData).toString();
  
    fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: urlEncodedData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          window.location.href = '/';
        } else {
          showToast(data.message || 'An unexpected error occurred. Please try again.');
        }
      })
      .catch((error) => {
        console.error('Login Error:', error);
        showToast('An unexpected error occurred. Please try again.');
      });
  }
  
  function handleLogout() {
    fetch('/logout', {
      method: 'GET',
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          showToast('Logout successful. You are now logged out.');
          window.location.href = '/login';
        } else {
          showToast(data.message || 'An unexpected error occurred. Please try again.');
        }
      })
      .catch((error) => {
        showToast('An unexpected error occurred. Please try again.');
      });
  }
  
  const loginForm = document.getElementById('login-form');
  if (loginForm) {
    loginForm.addEventListener('submit', handleLoginFormSubmit);
  }
  
  const logoutButton = document.getElementById('logout-button');
  if (logoutButton) {
    logoutButton.addEventListener('click', handleLogout);
  }
