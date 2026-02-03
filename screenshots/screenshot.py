import os
from datetime import datetime


async def take_screenshot(page, name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("screenshots", exist_ok=True)
    file_path = f"screenshots/{name}_{timestamp}.png"
    await page.screenshot(path=file_path, full_page=True)
    return file_path
