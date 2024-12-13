# Wing I
`Wing I is an REST API based Inspection Software written in FAST API which is used to  inspect issues in air crafts and other material surfaces. Wing I can be deployed from drones or from UGVs or anything that supports live camera streaming    `

## PROCEDURE
1. Get the images or videos from the drone to inspect.
2. Zip the image or videos.
3. Pass the Zipped payload to the Wing I API
4. You will be able to get the processed files as a zip to download.
5. Extract the zip and identify the detected defects.

## API MAPPING
### IMAGE PAYLOADS

| Command | Curl Request |
| --- | --- |
| `Version` | curl -X 'GET' \'http://localhost:2024/' \-H 'accept: application/json's |
| `Delete Files` | curl -X 'GET' \'http://localhost:2024/delete_files' \-H 'accept: application/json' |
| `Rust Detection` | curl -X 'POST' \'http://localhost:2024/rust_detection' \-H 'accept: application/json' \-H 'Content-Type: multipart/form-data' \-F 'input_file=@dataset.zip;type=application/zip' |
| `Dent Detection` |  curl -X 'POST' \'http://localhost:2024/dent_detection' \-H 'accept: application/json' \-H 'Content-Type: multipart/form-data' \-F 'input_file=@dataset.zip;type=application/zip'|
| `Color Fade Detection` | curl -X 'POST' \'http://localhost:2024/color_fade' \-H 'accept: application/json' \-H 'Content-Type: multipart/form-data' \-F 'input_file=@dataset.zip;type=application/zip' |



