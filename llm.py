import subprocess


class OllamaLLM:
    def __init__(self):
        # Start Ollama once and keep it running
        self.process = subprocess.Popen(
            ['ollama', 'run', 'mistral'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )

    def send_prompt(self, prompt):
        # Send the prompt + newline to Ollama
        self.process.stdin.write(prompt + "\n")
        self.process.stdin.flush()

        # Read one line response from Ollama
        response = self.process.stdout.readline().strip()
        return response

    def close(self):
        self.process.stdin.close()
        self.process.terminate()
        self.process.wait()
