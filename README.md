# Prequin assessment to write a production grade code.

Production grade code is:

- **Robust**
- **Scalable**
- **Easy to maintain**

Considerations taken at API level:
    
- **FastAPI**: High Performance web framework to build API. Provides interactive API Documentation OOB.
- **Pydantic**: Provides data validation by shaping data, provides helpful error messages when data is invalid.
- **Asynchronous functions**: Endpoints defined with `async def` we use `asyncio` to handle long running operations without blocking server using concurrency.
- **Using seed for reproducibility**: To ensure returned vector is reproducible.

---

Best practices to ensure the code is ready for production:

- Unit Tests for endpoints
- Input Validation using pydantic
- Error handling for server errors, not found errors, & validation errors.
- Security Checks to ensure protection against vulnerabilities. FastAPI has built-in features to protect against common threats.
- Logging & Monitoring
- Documentation

