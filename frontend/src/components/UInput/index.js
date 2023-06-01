// Components
import TextField from '@mui/material/TextField';

// Style
import './style.scss';

const UInput = ({
    placeholder = '',
    onChange,
    onFocus,
    onClick,
    value,
    id,
    inputError,
    errorText,
    errorClass,
    rows,
    multiline,
    minRows,
    maxRows,
    className,
    type,
    required,
    disabled,
}) => {

    return (
        <>
            <div className="input-field-wrapper">
                <TextField
                    id={`outlined-basic ${id}`}
                    label={placeholder}
                    variant="filled"
                    fullWidth={true}
                    onChange={onChange}
                    onFocus={onFocus}
                    onClick={onClick}
                    value={value}
                    error={inputError}
                    type={type}
                    name="username"
                    autoComplete="new-password"
                    rows={rows}
                    multiline={multiline}
                    minRows={minRows}
                    maxRows={maxRows}
                    className={className}
                    InputProps={{ disableUnderline: true }}
                    required={required}
                    disabled={disabled}
                // InputLabelProps={{ shrink: value ? true : false }}
                />
            </div>
            <div className={`error-message ${errorClass}`}>
                {errorText}
            </div>
        </>
    )
}

export default UInput
