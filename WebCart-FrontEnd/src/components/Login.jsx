import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Login = () => {
    const [isRegister, setIsRegister] = useState(false);
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage("");
        setError("");

        try {
            if (isRegister) {
                const response = await axios.post(
                    "http://localhost:8081/api/auth/register",
                    { username, password }
                );
                setMessage("Registration successful! You can now login.");
                setIsRegister(false);
                setUsername("");
                setPassword("");
            } else {
                const response = await axios.post(
                    "http://localhost:8081/api/auth/login",
                    { username, password }
                );
                localStorage.setItem("token", response.data.token);
                localStorage.setItem("username", response.data.username);
                navigate("/");
                window.location.reload();
            }
        } catch (err) {
            setError(
                err.response?.data?.error || "Something went wrong. Please try again."
            );
        }
    };

    return (
        <div
            className="d-flex justify-content-center align-items-center"
            style={{ minHeight: "100vh", paddingTop: "80px" }}
        >
            <div className="card shadow" style={{ width: "400px" }}>
                <div className="card-body p-4">
                    <h3 className="card-title text-center mb-4">
                        {isRegister ? "Register" : "Login"}
                    </h3>

                    {message && (
                        <div className="alert alert-success" role="alert">
                            {message}
                        </div>
                    )}
                    {error && (
                        <div className="alert alert-danger" role="alert">
                            {error}
                        </div>
                    )}

                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                            <label htmlFor="username" className="form-label">
                                Username
                            </label>
                            <input
                                type="text"
                                className="form-control"
                                id="username"
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                                required
                            />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="password" className="form-label">
                                Password
                            </label>
                            <input
                                type="password"
                                className="form-control"
                                id="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                            />
                        </div>
                        <button type="submit" className="btn btn-primary w-100 mb-3">
                            {isRegister ? "Register" : "Login"}
                        </button>
                    </form>

                    <div className="text-center">
                        <span>
                            {isRegister
                                ? "Already have an account? "
                                : "Don't have an account? "}
                        </span>
                        <button
                            className="btn btn-link p-0"
                            onClick={() => {
                                setIsRegister(!isRegister);
                                setMessage("");
                                setError("");
                            }}
                        >
                            {isRegister ? "Login" : "Register"}
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Login;
