import React from 'react'
import './style.scss'
import Button from '../../../components/Button/index'
import UInput from '../../../components/UInput/index'
import { Divider } from '@mui/material'
import {
    GoogleLoginButton,
    FacebookLoginButton,
    LinkedInLoginButton,
} from "react-social-login-buttons";

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
                    <Divider className='signin-divider'>or sign in with</Divider>
                    <div className='social-login-btn-wrapper'>
                        <GoogleLoginButton className='google-login-btn' />
                        <FacebookLoginButton className='facebook-login-btn' />
                        <LinkedInLoginButton className='linkedin-login-btn' />
                    </div>
                </div>
            </div>
        </div>
    )
}

export default LoginScreen;
