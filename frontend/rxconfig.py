import reflex as rx

config = rx.Config(
    app_name="app",
    api_url="http://localhost:3100",  # Backend URL
    backend_port=3100,
    frontend_port=3000,
    dev_mode=True,
)