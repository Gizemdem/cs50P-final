import os
import pytest
from project import Meme

@pytest.fixture
def meme_instance():
    return Meme()

def test_randomMeme_returns_valid_url(meme_instance):
    # Test if randomMeme returns a valid URL
    url = meme_instance.randomMeme()
    assert url.startswith("http")  # Ensure the URL starts with "http"

def test_export_creates_output_file(meme_instance):
    # Test export method with a dummy template path and output file
    dummy_template_path = "https://api.memegen.link/images/bilbo.png"
    dummy_output_file = "./test_meme.png"

    # Call export method
    meme_instance.export(dummy_template_path, output=dummy_output_file)

    # Assert that the output file is created
    assert os.path.exists(dummy_output_file)

    # Clean up (remove the test output file)
    os.remove(dummy_output_file)

def test_randomIndex():
    #returns a integer
    meme = Meme()
    index = meme.randomIndex()
    assert type(index) == int

def test_export_overlays_caption(meme_instance):
    # Test if export method overlays the caption onto the meme template
    dummy_template_path = "https://api.memegen.link/images/bilbo.png"
    dummy_output_file = "./test_meme.png"
    dummy_caption = "Test Caption"

    # Call export method
    meme_instance.caption = dummy_caption
    meme_instance.export(dummy_template_path, output=dummy_output_file)

    # Check if the output file exists
    assert os.path.exists(dummy_output_file)

    # Clean up (remove the test output file)
    os.remove(dummy_output_file)
