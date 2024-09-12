use pyo3::prelude::*;
use rustypath::RPath;


#[pyclass]
pub struct Scanner{
    directory: RPath,
    contents: Vec<RPath>,
}

#[pymethods]
impl Scanner {
    #[new]
    pub fn new(directory: &str) -> PyResult<Self> {
        Ok(Self {
            directory: RPath::from(directory),
            contents: Vec::new(),
        })
    }

    pub fn scan(&mut self) -> PyResult<()> {
        let mut content: Vec<RPath> = Vec::new();
        let mut dirs: Vec<RPath> = vec![self.directory.clone()];

        while let Some(current_dir) = dirs.pop() {
            for entry in current_dir.read_dir()? {
                let entry = entry?;
                let path = entry.path();

                if path.is_dir() {
                    dirs.push(RPath::from(path));
                } else {
                    content.push(RPath::from(path));
                }
            }
        }

        self.contents = content;

        Ok(())
    }

    pub fn files(&self) -> PyResult<Vec<RPath>> {
        Ok(self.contents.clone())
    }

    pub fn isolate(&mut self, r#type: &str) -> PyResult<Vec<RPath>> {
        let mut isolated: Vec<RPath> = Vec::new();

        for file in &self.contents {
            if file.if_extension(r#type) {
                isolated.push(file.to_owned());
            }
        }

        Ok(isolated)
    }
}