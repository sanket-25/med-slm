from huggingface_hub import hf_hub_download

file_path = hf_hub_download(
    repo_id="elsabado/Comprehensive-Medical-QA-Dataset",
    filename="medical-dataset.csv",
    repo_type="dataset",
    local_dir="."
)

print("Downloaded to:", file_path)