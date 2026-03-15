# Algorithm Visualizer

Watch sorting algorithms work step by step — pick an algorithm, generate a random array, and play through each comparison and swap as an animated bar chart.

**Supported algorithms:** Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort

---

## Running with Docker (recommended)

The easiest way. You only need [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed.

```bash
docker compose up --build
```

Then open **http://localhost** in your browser. That's it.

To stop it, press `Ctrl+C`.

---

## Running locally (for developers)

You'll need **Python 3.10+** and **Node.js 18+** installed.

**Terminal 1 — backend:**
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Terminal 2 — frontend:**
```bash
cd frontend
npm install
npm start
```

Then open **http://localhost:3000**.

---

## How to use it

1. Pick an algorithm from the dropdown
2. Click **Generate Steps** to send the array to the backend
3. Click **Play** to watch the sort animate
4. Use the speed slider to slow it down or speed it up
5. Click **New Array** to shuffle and start over

Bar colors during playback:
- **Blue** — unsorted
- **Yellow** — currently being compared
- **Red** — being swapped
- **Green** — fully sorted
