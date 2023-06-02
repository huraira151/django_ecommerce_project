import React from 'react'
import Button from '../../components/Button'

import { history } from '../../reduxStore/store'

const NotFound = () => {


    return (
        <div className='page-not-found'
            style={{
                height: '100vh',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                flexDirection: 'column'
            }}>
            <p
                style={{
                    color: '#30D5C8',
                    fontWeight: 600,
                    fontSize: 50,
                    textAlign: 'center',
                    lineHeight: '56px'
                }}
            >Oops!</p>
            <p
                style={{ textAlign: 'center' }}
            >
                Sorry, we can't find that page.
                <br />
                You'll find lots to explore on the home page.

            </p>
            <Button
                title='Home'
                onClick={() => history.push('/admin/home')}
            />
        </div>
    )
}


export default NotFound