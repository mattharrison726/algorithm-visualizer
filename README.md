# Algorithm Visualizer

Watch sorting algorithms work step by step — pick an algorithm, generate a random array, and play through each comparison and swap as an animated bar chart.

**Supported algorithms:** Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort

---

## How to run it

### Step 1 — Install Docker Desktop

Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/) for your operating system (Mac or Windows). Once installed, open it and let it finish starting up. You'll see the Docker whale icon in your menu bar (Mac) or system tray (Windows) when it's ready.

### Step 2 — Open a terminal in the project folder

**On Mac:**
1. Open **Finder** and navigate to the `algorithm-visualizer` folder
2. Right-click the folder and select **"New Terminal at Folder"**
   - If you don't see that option, open **Terminal** from Applications → Utilities, then type `cd ` (with a space), drag the folder into the Terminal window, and press Enter

**On Windows:**
1. Open **File Explorer** and navigate to the `algorithm-visualizer` folder
2. Click the address bar at the top, type `cmd`, and press Enter

### Step 3 — Start the app

In the terminal, type the following and press Enter:

```
docker compose up --build
```

The first time you run this it will take a few minutes to download and build everything. You'll see a lot of text scrolling — that's normal. Wait until the output settles and you see messages from both `frontend` and `backend`.

### Step 4 — Open the app

Once it's running, click this link to open the app in your browser:

**[http://localhost](http://localhost)**

### Stopping the app

Go back to the terminal and press `Ctrl+C`. The app will shut down.

---

## How to use it

1. Pick an algorithm from the dropdown
2. Click **Generate Steps** to load a random array
3. Click **Play** to watch the sort animate
4. Use the speed slider to slow it down or speed it up
5. Click **New Array** to shuffle and start over

Bar colors during playback:
- **Blue** — unsorted
- **Yellow** — currently being compared
- **Red** — being swapped
- **Green** — fully sorted

---

## For developers

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
