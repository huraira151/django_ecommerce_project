import React from 'react'
import Header from '../../components/Header';
import './style.scss'

const Home = () => {
    return (
        <Header>
            <div className='home-wrapper'>
                <div className='home-section'>
                    Welcome
                </div>
            </div>
        </Header>
    )
}

export default Home;
