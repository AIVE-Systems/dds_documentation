# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "AIVE DDS Documentation"
copyright = "2025, Toby Godfrey"
author = "Toby Godfrey"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.graphviz"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_nefertiti"
html_static_path = ["_static"]
html_theme_options = {
    "style": "orange",
    "header_links": [
        {
            "text": "Overview",
            "link": "overview",
        },
        {
            "text": "User Guide",
            "link": "user_guide",
        },
    ],
    "logo": "logo.png",
    "logo_width": 24,
    "logo_height": 24,
}
