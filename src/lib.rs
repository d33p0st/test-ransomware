mod scan;

use pyo3::prelude::*;

#[pymodule]
#[pyo3(name = "rlib")]
fn rlib(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<scan::Scanner>()?;
    Ok(())
}