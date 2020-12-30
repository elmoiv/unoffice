from zipupdate import UpdateableZipFile, ZipFile, shutil

# Extract file from zip
def extract_archive(org, zip_dist, file_dist):
    with ZipFile(org) as z:
        with z.open(zip_dist) as zf, open(file_dist, 'wb') as f:
            shutil.copyfileobj(zf, f)

# Extract all files inside zip folder
def extract_archive_all(org, zip_dist):
    with ZipFile(org) as z:
        for _file in filter(lambda i: i.startswith(zip_dist), z.namelist()):
            with z.open(_file) as zf, open(_file.split('/')[-1], 'wb') as f:
                shutil.copyfileobj(zf, f)

# Add the extracted file again safely
def update_archive(org, _file, zip_dist):
    with UpdateableZipFile(org, "a") as o:
        o.write(_file, zip_dist)