# Потрібно розробити програму, яка імітує приймання й обробку заявок:
# програма має автоматично генерувати нові заявки
# (ідентифіковані унікальним номером або іншими даними),
# додавати їх до черги,
# а потім послідовно видаляти з черги для "обробки",
# імітуючи таким чином роботу сервісного центру.

import uuid
from datetime import datetime
from queue import Queue

# # ANSI escape codes for colored output
COLOR_BLUE = "\\033[94m"
COLOR_YELLOW = "\\033[93m"
COLOR_RESET = "\\033[0m"


class ServiceCenterQueue:
    """Class to simulate a service center request queue."""

    def __init__(self):
        self.queue = Queue()
        print("ServiceCenter is opened.")
        self.running = True

    def generate_request(self, request_message="New Request"):
        """Generate a new request and add it to the queue."""
        if self.running:
            request = {
                "id": str(uuid.uuid4()),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "message": request_message,
            }
            self.queue.put(request)
            print(
                f"New request added to the queue: {request}. Requests in queue: {self.queue.qsize()}"
            )

    def process_request(self):
        """Process requests from the queue."""
        if self.running:
            if not self.queue.empty():
                request = self.queue.get()
                print(
                    f"Processing request: {request}. Requests left in queue: {self.queue.qsize()}"
                )
            else:
                print("Queue is empty, waiting for new requests...")

    def stop(self):
        """Stop the request queue processing."""
        self.running = False
        print("ServiceCenter is closed.")


if __name__ == "__main__":

    print(
        "Press G to generate request, press P to process request. Press Ctrl+C to exit."
    )
    request_queue = ServiceCenterQueue()

    i = 1
    try:
        while True:
            cmd = input("> ").strip().lower()
            if cmd == "g":
                request_queue.generate_request(f"Service Request {i}")
                i += 1
            elif cmd == "p":
                request_queue.process_request()
            else:
                print(
                    "Invalid command. Press G to generate request, P to process request."
                )
    except KeyboardInterrupt:
        print("Console closed by user (Ctrl+C).")
    finally:
        request_queue.stop()
