from fastapi import APIRouter, UploadFile, File, Form
from app.utils.extract import extract_text
from app.utils.aligner import align_segments

import tempfile
import shutil
import os

router = APIRouter()

@router.post("/align")
async def align_files(
    source_file: UploadFile = File(...),
    target_file: UploadFile = File(...),
    src_lang: str = Form(...),
    tgt_lang: str = Form(...)
):

    with tempfile.TemporaryDirectory() as tmpdir:
        src_path = os.path.join(tmpdir, source_file.filename)
        tgt_path = os.path.join(tmpdir, target_file.filename)

        with open(src_path, "wb") as f:
            shutil.copyfileobj(source_file.file, f)

        with open(tgt_path, "wb") as f:
            shutil.copyfileobj(target_file.file, f)

        src_text = extract_text(src_path)
        tgt_text = extract_text(tgt_path)

        aligned = align_segments(src_text, tgt_text)

        return {"alignment": aligned}
