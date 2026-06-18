import pathlib

BASE = pathlib.Path(r"C:\Users\MSY\Desktop\insurance-website\src\app")

# globals.css
css = '''@import "tailwindcss";

::root {
  --background: #ffffff;
  --foreground: #171717;
  --primary: #1e40af;
  --primary-light: #3b82f6;
  --accent: #f59e0b;
}

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-primary: var(--primary);
  --color-primary-light: var(--primary-light);
  --color-accent: var(--accent);
  --font-sans: var(--font-geist-sans);
  --font-mono: var(--font-geist-mono);
}

body {
  background: var(--background);
  color: var(--foreground);
  font-family: var(--font-sans), Arial, Helvetica, sans-serif;
}

html {
  scroll-behavior: smooth;
}
'''
(BASE / "globals.css").write_text(css.strip(), encoding="utf-8")
print("globals.css updated")