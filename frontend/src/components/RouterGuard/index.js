import React from 'react'
import { Navigate, Outlet } from 'react-router-dom';
// import { history } from '../../reduxStore/store'

const RequireAuth = () => {
    const token = localStorage.getItem("token")

    return (
        token ? <Outlet /> : <Navigate to="/login" replace />
    )
}

export default RequireAuth;
