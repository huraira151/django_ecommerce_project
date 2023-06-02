import React from 'react'
import './style.scss'
import Button from '../../../components/Button/index'
import UInput from '../../../components/UInput/index'
import { Divider } from '@mui/material'
import GoogleIcon from '@mui/icons-material/Google';
import FacebookIcon from '@mui/icons-material/Facebook';
import LinkedInIcon from '@mui/icons-material/LinkedIn';

const SignUpScreen = () => {
    return (
        <div className='signup-section-wrapper'>
            <div className='signup-form-container'>
                <div className='signup-form-section'>
                    <h1>Sign Up</h1>
                    <UInput
                        placeholder='Name'
                        type='text'
                    />
                    <UInput
                        placeholder='Email'
                        type='email'
                        required={true}
                    />
                    <UInput
                        placeholder='Phone Number'
                        type='tel'
                    />
                    <UInput
                        placeholder='Address'
                        type='text'
                    />
                    <UInput
                        placeholder='Password'
                        type='password'
                        required={true}
                    />
                    <Button
                        title='Sign Up'
                        className='signup-btn'
                    />
                    <div className='signup-account-wrapper'>
                        <span className='already-account'>Already have an account! <a href="http://localhost:3000/login/">Login</a></span>
                    </div>
                    <Divider className='signup-divider'>or sign up with</Divider>
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

export default SignUpScreen;
