# Smart File Aligner

**Smart File Aligner** is a flexible tool that aligns textual content between source and target files, even if they are in different formats (e.g., `.txt`, `.pdf`, `.pptx`, `.docx`). The tool is designed for use cases like translation alignment or bilingual content review.

## 📌 Key Features

- Automatically detects language from filenames using ISO Alpha-2 codes (e.g., `_EN`, `_FR`, `_ZH`)
- Pairs files across source and target folders based on matching base filenames (ignoring extensions)
- Supports cross-format file alignment (e.g., `.txt` ↔ `.pptx`)
- Outputs aligned content in a CSV format, placing segments side-by-side
- Isolates unpaired segments into their own rows

## 🗂️ How It Works

1. **File Naming Convention**  
   The tool expects file names to end with an ISO Alpha-2 language code suffix:
    filename1_EN.txt
    filename1_FR.pptx
    somefile_ZH.pdf

2. **Source and Target Folders**  
You provide two folders:
- `Source`: Contains files like `filename1_EN.txt`
- `Target`: Contains corresponding translated files like `filename1_FR.pptx`

3. **File Pairing Logic**  
- The tool strips the language code and extension from the filenames (e.g., `filename1`).
- It finds matching base names in both folders (e.g., `filename1_EN.txt` ↔ `filename1_FR.pptx`).
- Only files with matching base names (before the last `_`) are paired for alignment.

4. **Alignment Process**  
- Content from each file pair is segmented (e.g., by sentence, paragraph).
- Segments from source and target are aligned side-by-side.
- If segments cannot be matched, they are listed independently in separate rows.

5. **Output Format**  
- A `.csv` file containing aligned (and unaligned) segments.
- Each row contains:
  ```
  Source Segment | Target Segment
  ```

## 📁 Example

If you have:

- `Source/contract_EN.txt`
- `Target/contract_FR.pdf`

The tool will:
- Extract the base name `contract`
- Detect `_EN` as source and `_FR` as target languages
- Align and export segments to a `contract_EN_FR.csv`

## 🚀 Usage

Instructions on how to run the tool coming soon.

---

Feel free to contribute, suggest improvements, or report issues via GitHub!
