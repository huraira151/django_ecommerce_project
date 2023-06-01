import React from 'react';

// Components
import Modal from 'react-bootstrap/Modal';
import { history } from '../../../reduxStore/store';
import { Images } from '../../../theme/Images';
import Button from '../../Button';
import UInput from '../../UInput';
import Image from '../../Image';

// Style
import './style.scss'

const AddDesignerModal = ({ showModal, setShowModal }) => {


    return (
        <>
            <Modal
                show={showModal}
                setShow={setShowModal}
                centered
                className='auth-modal reset-modal'
            >
                <Modal.Header>
                    <Modal.Title>
                        <div className="wrapper flex-justify-end w-100">
                            <div className="close-icon"
                                onClick={() => setShowModal(false)}
                            >
                                <Image
                                    src={Images.closeIcon}
                                />
                            </div>
                        </div>
                    </Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <div className="auth-modal-body-wrapper reset-modal-body-wrapper">
                        <div className='designer-input-fields'>
                            <UInput
                                placeholder="Full Name"
                                type='text'
                                className='designer-full-name'
                            />
                            <UInput
                                type='email'
                                placeholder='Email'
                                className='designer-email'
                            />
                        </div>
                        <Button
                            title="Add"
                            className="add-designer-button"
                            onClick={() => history.push('/admin/designers-list')}
                        />
                    </div>
                </Modal.Body>
            </Modal>
        </>

    );
}


export default AddDesignerModal;
