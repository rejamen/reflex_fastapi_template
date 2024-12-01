import reflex as rx
import logging
import aiohttp
import os

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

class State(rx.State):
    """The app state."""
    message: str = "Click the button to get message"
    
    async def get_message(self):
        try:
            async with aiohttp.ClientSession() as session:
                backend_ip_address = os.getenv("BACKEND_IP_ADDRESS", "localhost")
                response = await session.get(f"http://{backend_ip_address}:8000/api/message")
                data = await response.json()
                self.message = data["message"]
        except Exception as e:
            _logger.error(f"Error fetching message: {e}")
            self.message = f"Error: {str(e)}"
    
def index() -> rx.Component:
    _logger.info("Rendering index page")
    return rx.vstack(
        rx.heading("Reflex Frontend Demo"),
        rx.text(State.message),
        rx.button("Get Message", on_click=State.get_message),
        spacing="9",
        padding="20px",
    )

app = rx.App()
app.add_page(index)