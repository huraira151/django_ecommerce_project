import React from 'react'
import './style.scss'
import Button from '../../../components/Button/index'
import UInput from '../../../components/UInput/index'
import { Divider } from '@mui/material'
import GoogleIcon from '@mui/icons-material/Google';
import FacebookIcon from '@mui/icons-material/Facebook';
import LinkedInIcon from '@mui/icons-material/LinkedIn';

const LoginScreen = () => {
    return (
        <div className='login-section-wrapper'>
            <div className='login-form-container'>
                <div className='login-form-section'>
                    <h1>Login</h1>
                    <UInput
                        placeholder='Email'
                        type='email'
                        required={true}
                    />
                    <UInput
                        placeholder='Password'
                        type='password'
                        required={true}
                    />
                    <Button
                        title='Sign In'
                        className='signin-btn'
                    />
                    <div className='account-wrapper'>
                        <a className='forgot-pass' href="http://localhost:3000/signup/">Forgot Password?</a>
                        <span className='create-account'>Dont have an account! <a href="http://localhost:3000/signup/">Create one</a></span>
                    </div>
                    <Divider className='signin-divider'>or sign in with</Divider>
                    <div className='social-login-btn-wrapper'>
                        <GoogleIcon style={{
                            color: '#db4437',
                            marginRight: "10px",
                            cursor: "pointer",
                            fontSize: "30px"
                        }} className='google-icon' />
                        <FacebookIcon style={{
                            color: '#3b5998',
                            marginRight: "10px",
                            cursor: "pointer",
                            fontSize: "30px"
                        }} className='google-icon' />
                        <LinkedInIcon style={{
                            color: '#0077b5',
                            cursor: "pointer",
                            fontSize: "30px",
                        }} className='google-icon' />
                    </div>
                </div>
            </div>
        </div>
    )
}

export default LoginScreen;