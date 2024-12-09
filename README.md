# WingEye
<li>Fast API based Inspection Server</li>
<li>Can check for Rust, Dents, Cracks and Colour Fading using different endpoints</li>

## How it works
<li>The image(s) are sent to the server as a zip file</li>
<li>For now only Rust detection is implemented</li>
<li>The images are extracted from the zip file and temporarily stored in the server in Uploaded_Files</li>
<li>The zip file is now deleted</li>
<li>The images  are then processed and stored in Processed_files</li>
<li>Once all the images are processed, they are compressed into a new zip folder and returned as a downloadable file</li>
<li>Any images in the Uploaded_Files or Processed_Files folder are deleted</li>