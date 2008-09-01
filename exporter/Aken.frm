VERSION 5.00
Object = "{F9043C88-F6F2-101A-A3C9-08002B2F49FB}#1.2#0"; "COMDLG32.OCX"
Begin VB.Form Aken 
   Caption         =   "Form1"
   ClientHeight    =   2925
   ClientLeft      =   60
   ClientTop       =   375
   ClientWidth     =   7230
   BeginProperty Font 
      Name            =   "Verdana"
      Size            =   9
      Charset         =   186
      Weight          =   400
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   LinkTopic       =   "Form1"
   ScaleHeight     =   2925
   ScaleWidth      =   7230
   StartUpPosition =   3  'Windows Default
   Begin MSComDlg.CommonDialog FileAccess 
      Left            =   3285
      Top             =   90
      _ExtentX        =   847
      _ExtentY        =   847
      _Version        =   393216
   End
   Begin VB.TextBox txtDatabaseFile 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BorderStyle     =   0  'None
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   285
      Left            =   1845
      Locked          =   -1  'True
      TabIndex        =   8
      TabStop         =   0   'False
      Top             =   945
      Width           =   5235
   End
   Begin VB.TextBox txtLibraryName 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BorderStyle     =   0  'None
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   285
      Left            =   1845
      Locked          =   -1  'True
      TabIndex        =   6
      TabStop         =   0   'False
      Top             =   585
      Width           =   5235
   End
   Begin VB.CheckBox chkDeleteRows 
      Alignment       =   1  'Right Justify
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      Caption         =   "Delete old rows:"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000008&
      Height          =   285
      Left            =   135
      TabIndex        =   4
      Top             =   1620
      Width           =   1905
   End
   Begin VB.TextBox txtExportFile 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BorderStyle     =   0  'None
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   285
      Left            =   1845
      Locked          =   -1  'True
      TabIndex        =   3
      TabStop         =   0   'False
      Top             =   1305
      Width           =   5235
   End
   Begin VB.CommandButton Nupp_Export 
      Caption         =   "Export"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   420
      Left            =   5715
      TabIndex        =   2
      Top             =   2340
      Width           =   1365
   End
   Begin VB.TextBox txtLibraryID 
      Appearance      =   0  'Flat
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   285
      Left            =   1845
      MaxLength       =   3
      TabIndex        =   1
      Top             =   225
      Width           =   780
   End
   Begin VB.Label Label4 
      Alignment       =   1  'Right Justify
      Appearance      =   0  'Flat
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "Database file:"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000008&
      Height          =   285
      Left            =   90
      TabIndex        =   9
      Top             =   945
      Width           =   1650
   End
   Begin VB.Label Label3 
      Alignment       =   1  'Right Justify
      Appearance      =   0  'Flat
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "Library name:"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000008&
      Height          =   285
      Left            =   90
      TabIndex        =   7
      Top             =   585
      Width           =   1650
   End
   Begin VB.Label Label2 
      Alignment       =   1  'Right Justify
      Appearance      =   0  'Flat
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "SQL file:"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000008&
      Height          =   285
      Left            =   90
      TabIndex        =   5
      Top             =   1305
      Width           =   1650
   End
   Begin VB.Label Label1 
      Alignment       =   1  'Right Justify
      Appearance      =   0  'Flat
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "Library ID:"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000008&
      Height          =   285
      Left            =   90
      TabIndex        =   0
      Top             =   225
      Width           =   1650
   End
   Begin VB.Shape Shape1 
      BackColor       =   &H00FFFFFF&
      BackStyle       =   1  'Opaque
      Height          =   2175
      Left            =   -45
      Top             =   -45
      Width           =   7350
   End
End
Attribute VB_Name = "Aken"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Dim gConnect As ADODB.Connection
Dim gRS As ADODB.Recordset

Private Sub Form_Load()
    Me.Caption = App.ProductName & " - " & App.Major & "." & App.Minor & "." & App.Revision

    FileAccess.CancelError = False
    FileAccess.Filter = "ARX-Raamat Database File|*.mdb"
    FileAccess.ShowOpen

    If LenB(FileAccess.FileName) = 0 Then
        End
    Else
        txtDatabaseFile.Text = FileAccess.FileName
        txtExportFile.Text = Left(FileAccess.FileName, Len(FileAccess.FileName) - 4) & ".sql"
        
        Set gConnect = New ADODB.Connection
        Set gRS = New ADODB.Recordset
        
        gConnect.Open "PROVIDER=Microsoft.Jet.OLEDB.4.0;Data Source=""" & FileAccess.FileName & """;"
        
        gRS.Open "SELECT SETUP_VALUE FROM X_SETUP WHERE SETUP_KEY = ""ASUTUS""", gConnect
        txtLibraryName.Text = gRS("SETUP_VALUE")
        gRS.Close
        gRS.Open "SELECT SETUP_VALUE FROM X_SETUP WHERE SETUP_KEY = ""VERSIOON""", gConnect
        txtLibraryName.Text = txtLibraryName.Text & " (" & gRS("SETUP_VALUE") & ")"
        gRS.Close
        
    End If
    
End Sub

Private Sub txtLibraryID_GotFocus()
    txtLibraryID.SelStart = 0
    txtLibraryID.SelLength = Len(txtLibraryID.Text)
End Sub

Private Sub Nupp_Export_Click()
    If IsNumeric(txtLibraryID.Text) = False Or Trim(txtLibraryID.Text) = "1" Then
        MsgBox "Library ID must be number!", vbCritical
        txtLibraryID.SetFocus
        Exit Sub
    End If
    
    Export
End Sub

Private Sub Export()
    Dim myFilename As String
    
    Screen.MousePointer = vbHourglass
    
    Open txtExportFile.Text For Output As #1
    Print #1, "## Library ID:     " & txtLibraryID.Text
    Print #1, "## Library Name:   " & txtLibraryName.Text
    Print #1, "## Export started: " & Format(Now, "yyyy-mm-dd Hh:Nn:Ss")
    Close #1
    
'    Export_Inventariraamat
    
    Export_Klass
    Export_Lugeja

    Export_Meedia
    Export_MeediaEksemplar

    Export_Andmekandja
    Export_Keel
    Export_Liik
    Export_Marksona
    Export_Valjaandja

    Export_Autor

    Export_Meedia_Field "KLASS", 6
    Export_Meedia_Field "ILMUMISAASTA", 7
    Export_Meedia_Field "RIIUL", 8

'    Export_Saatedokument
'    Export_Mahakandmisakt

    
    Open txtExportFile.Text For Append As #1
    Print #1, ""
    Print #1, ""
    Print #1, ""
    Print #1, "## Library ID:   " & txtLibraryID.Text
    Print #1, "## Library Name: " & txtLibraryName.Text
    Print #1, "## Export ended: " & Format(Now, "yyyy-mm-dd Hh:Nn:Ss")
    Print #1, ""
    Print #1, ""
    Print #1, ""
    Print #1, "## END "
    Close #1
    
    Screen.MousePointer = vbDefault
    
    MsgBox FileAccess.FileName & " exported to " & txtExportFile.Text, vbInformation
    
    End
    
End Sub







Private Sub Export_Inventariraamat()
    Dim myString As String
    Dim myN As Integer

    Open Left(txtExportFile.Text, Len(txtExportFile.Text) - 4) & "_INV.csv" For Output As #1
    
    gRS.Open "SELECT MEEDIA.MEEDIA_LIIK, MEEDIA_EKSEMPLAR.INVENTARI_NUMBER AS INVENTARI_NR, MEEDIA.PEALKIRI, MEEDIA.KLASS, MEEDIA.ILMUMISAASTA, MEEDIA_EKSEMPLAR.NUMBER AS PERIOODIKA_NR, ANDMEKANDJA.NIMI AS ANDMEKANDJA, LIIK.NIMI AS LIIK, KEEL.NIMI AS KEEL, VALJAANDJA.NIMI AS VALJAANDJA, MEEDIA.RIIUL, MEEDIA.MARKUSED AS MEEDIA_MARKUSED, Format([MEEDIA_EKSEMPLAR].[SISSEKANDE_KUUPAEV],""yyyy-mm-dd"") AS SISSEKANDE_KPV, MEEDIA_EKSEMPLAR.HIND, MEEDIA_EKSEMPLAR.KOGUS, SAATEDOKUMENT.DOKUMENDI_NUMBER AS SD_NUMBER, Format([SAATEDOKUMENT].[KUUPAEV],""yyyy-mm-dd"") AS SD_KUUPAEV, VALJAANDJA_1.NIMI AS SD_VALJAANDJA, MAHAKANDMISAKT.AKTI_NUMBER AS MA_NUMBER, Format([MAHAKANDMISAKT].[KUUPAEV],""yyyy-mm-dd"") AS MA_KUUPAEV, MAHAKANDMISAKT.POHJUS AS MA_POHJUS, MEEDIA_EKSEMPLAR.MARKUSED AS EKSEMPLAR_MARKUSED " _
           & "FROM (((((((MEEDIA_EKSEMPLAR LEFT JOIN MEEDIA ON MEEDIA_EKSEMPLAR.MEEDIA_FK = MEEDIA.MEEDIA_ID) LEFT JOIN VALJAANDJA ON MEEDIA.VALJAANDJA_FK = VALJAANDJA.VALJAANDJA_ID) LEFT JOIN ANDMEKANDJA ON MEEDIA.ANDMEKANDJA_FK = ANDMEKANDJA.ANDMEKANDJA_ID) LEFT JOIN LIIK ON MEEDIA.LIIK_FK = LIIK.LIIK_ID) LEFT JOIN KEEL ON MEEDIA.KEEL_FK = KEEL.KEEL_ID) LEFT JOIN SAATEDOKUMENT ON MEEDIA_EKSEMPLAR.SAATEDOKUMENT_FK = SAATEDOKUMENT.SAATEDOKUMENT_ID) LEFT JOIN VALJAANDJA AS VALJAANDJA_1 ON SAATEDOKUMENT.VALJAANDJA_FK = VALJAANDJA_1.VALJAANDJA_ID) LEFT JOIN MAHAKANDMISAKT ON MEEDIA_EKSEMPLAR.MAHAKANDMISAKT_FK = MAHAKANDMISAKT.MAHAKANDMISAKT_ID " _
           & "ORDER BY MEEDIA.MEEDIA_LIIK, TRIM(MEEDIA_EKSEMPLAR.INVENTARI_NUMBER), TRIM(MEEDIA.PEALKIRI), TRIM(MEEDIA.KLASS)", gConnect
    
    myString = ""
    For myN = 0 To gRS.Fields.Count - 1
        myString = myString & ";" & gRS(myN).Name
    Next myN
    Print #1, Mid(myString, 2)
    
    Do Until gRS.EOF
        
        myString = ""
        For myN = 0 To gRS.Fields.Count - 1
            If IsNull(gRS(myN)) Then
                myString = myString & ";"
            Else
                myString = myString & ";" & IIf(IsNull(Trim(gRS(myN))) = True, "", Replace(Trim(gRS(myN)), ";", ","))
            End If
        Next myN
        
        Print #1, Mid(myString, 2)
        
        gRS.MoveNext
    Loop
    gRS.Close
    
    Close #1

End Sub







Private Sub Export_Klass()
    Dim myString As String

    Open txtExportFile.Text For Append As #1
    
    Print #1, ""
    Print #1, ""
    Print #1, ""
    Print #1, "## KLASS ##"
    Print #1, ""
    If chkDeleteRows.Value = vbChecked Then Print #1, "DELETE FROM usergroups WHERE old_id LIKE '" & txtLibraryID.Text & "-%';"
 
    gRS.Open "SELECT * FROM klass ORDER BY KLASSI_NUMBER, KLASSI_TAHT", gConnect
    Do Until gRS.EOF
        
        myString = ""
        myString = myString & "INSERT INTO usergroups SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldString("old_id", txtLibraryID.Text & "-" & gRS("KLASS_ID"))
        myString = myString & FieldString("name", Trim(gRS("KLASSI_NUMBER")) & " " & Trim(gRS("KLASSI_TAHT")))
        myString = myString & FieldString("note", gRS("MARKUSED"))
        myString = myString & ";"
        
        Print #1, myString
        gRS.MoveNext
    Loop
    gRS.Close
    
    Close #1

End Sub

Private Sub Export_Lugeja()
    Dim myString As String
    
    Open txtExportFile.Text For Append As #1
    
    Print #1, ""
    Print #1, ""
    Print #1, ""
    Print #1, "## LUGEJA ##"
    Print #1, ""
    If chkDeleteRows.Value = vbChecked Then Print #1, "DELETE FROM users WHERE old_id LIKE '" & txtLibraryID.Text & "-%' AND username IS NULL;"
    
    gRS.Open "SELECT * FROM lugeja ORDER BY NIMI, EESNIMI", gConnect
    Do Until gRS.EOF
        
        myString = ""
        myString = myString & "INSERT INTO users SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldString("old_id", txtLibraryID.Text & "-" & gRS("LUGEJA_ID"))
        myString = myString & FieldSelect("usergroups", "usergroup_id", gRS("KLASS_FK"))
        myString = myString & FieldString("firstname", gRS("EESNIMI"))
        myString = myString & FieldString("lastname", gRS("NIMI"))
        myString = myString & FieldString("address", gRS("AADRESS"))
        myString = myString & FieldString("city", gRS("LINN"))
        myString = myString & FieldString("county", getMaakond(gRS("MAAKOND_FK")))
        myString = myString & FieldString("zip", gRS("POSTIINDEKS"))
        myString = myString & FieldString("phone", gRS("TELEFON"))
        myString = myString & FieldString("note", gRS("MARKUSED"))
        myString = myString & ";"
        
        Print #1, myString
        gRS.MoveNext
    Loop
    gRS.Close

    Close #1

End Sub







Private Sub Export_Meedia()
    Dim myString As String
    
    Open txtExportFile.Text For Append As #1
    
    Print #1, ""
    Print #1, ""
    Print #1, ""
    Print #1, "## MEEDIA ##"
    Print #1, ""
    If chkDeleteRows.Value = vbChecked Then Print #1, "DELETE FROM media WHERE old_id LIKE '" & txtLibraryID.Text & "-%';"
    
    gRS.Open "SELECT * FROM meedia ORDER BY PEALKIRI", gConnect
    Do Until gRS.EOF
        
        myString = ""
        myString = myString & "INSERT INTO media SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldString("old_id", txtLibraryID.Text & "-" & gRS("MEEDIA_ID"))
        Select Case gRS("MEEDIA_LIIK")
            Case "RA"
                myString = myString & FieldNumber("mediatype_id", 1)
            Case "OP"
                myString = myString & FieldNumber("mediatype_id", 2)
            Case "TV"
                myString = myString & FieldNumber("mediatype_id", 3)
            Case "PE"
                myString = myString & FieldNumber("mediatype_id", 4)
            Case "AV"
                myString = myString & FieldNumber("mediatype_id", 5)
            Case "MK"
                myString = myString & FieldNumber("mediatype_id", 6)
        End Select
        myString = myString & FieldString("title", gRS("PEALKIRI"))
        myString = myString & FieldString("note", gRS("MARKUSED"))
        myString = myString & ";"
        
        Print #1, myString
        gRS.MoveNext
    Loop
    gRS.Close

    Close #1

End Sub







Private Sub Export_Andmekandja()
    Dim myString As String

    Close #1
    Open txtExportFile.Text For Append As #1

    Print #1, ""
    Print #1, ""
    Print #1, ""
    Print #1, "## ANDMEKANDJA ##"
    Print #1, ""
    
    gRS.Open "SELECT DISTINCT TRIM(NIMI) AS NIMI FROM andmekandja ORDER BY TRIM(NIMI)", gConnect
    Do Until gRS.EOF

        myString = ""
        myString = myString & "INSERT IGNORE INTO tags SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldNumber("tagtype_id", 1)
        myString = myString & FieldString("nimi", gRS("NIMI"))
        myString = myString & ";"

        Print #1, myString

        gRS.MoveNext
    Loop
    gRS.Close

    Print #1, ""
    Print #1, ""
    Print #1, ""
    
    If chkDeleteRows.Value = vbChecked Then Print #1, "DELETE FROM media_tags WHERE old_id LIKE '" & txtLibraryID.Text & "-%' AND tag_id IN (SELECT id FROM tags WHERE tagtype_id = 1);"

    gRS.Open "SELECT MEEDIA_ID, TRIM(NIMI) AS NIMI FROM meedia, andmekandja WHERE ANDMEKANDJA_FK = ANDMEKANDJA_ID AND LEN(TRIM(NIMI))>0 ORDER BY MEEDIA_ID", gConnect
    Do Until gRS.EOF

        myString = ""
        myString = myString & "INSERT INTO media_tags SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldString("old_id", txtLibraryID.Text & "-")
        myString = myString & FieldSelect("media", "media_id", gRS("MEEDIA_ID"))
        myString = myString & ", tag_id = (SELECT id FROM tags WHERE UPPER(TRIM(name)) = '" & UCase(gRS("NIMI")) & "' and tagtype_id = 1 LIMIT 0, 1)"
        myString = myString & ";"

        Print #1, myString

        gRS.MoveNext
    Loop
    gRS.Close

    Close #1

End Sub

Private Sub Export_Keel()
    Dim myString As String
    
    Open txtExportFile.Text For Append As #1
    
    Print #1, ""
    Print #1, ""
    Print #1, ""
    Print #1, "## KEEL ##"
    Print #1, ""
    
    gRS.Open "SELECT DISTINCT TRIM(NIMI) AS NIMI FROM keel ORDER BY TRIM(NIMI)", gConnect
    Do Until gRS.EOF
        
        myString = ""
        myString = myString & "INSERT IGNORE INTO tags SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldNumber("tagtype_id", 2)
        myString = myString & FieldString("name", gRS("NIMI"))
        myString = myString & ";"
        
        Print #1, myString
        gRS.MoveNext
    Loop
    gRS.Close

    Print #1, ""
    Print #1, ""
    Print #1, ""
    
    If chkDeleteRows.Value = vbChecked Then Print #1, "DELETE FROM media_tags WHERE old_id LIKE '" & txtLibraryID.Text & "-%' AND tag_id IN (SELECT id FROM tags WHERE tagtype_id = 2);"

    gRS.Open "SELECT MEEDIA_ID, TRIM(NIMI) AS NIMI FROM meedia, keel WHERE KEEL_FK = KEEL_ID AND LEN(TRIM(NIMI))>0 ORDER BY MEEDIA_ID", gConnect
    Do Until gRS.EOF

        myString = ""
        myString = myString & "INSERT INTO media_tags SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldString("old_id", txtLibraryID.Text & "-")
        myString = myString & FieldSelect("media", "media_id", gRS("MEEDIA_ID"))
        myString = myString & ", tag_id = (SELECT id FROM tags WHERE UPPER(TRIM(name)) = '" & UCase(gRS("NIMI")) & "' and tagtype_id = 2 LIMIT 0, 1)"
        myString = myString & ";"

        Print #1, myString

        gRS.MoveNext
    Loop
    gRS.Close

    Close #1

End Sub

Private Sub Export_Liik()
    Dim myString As String
    
    Open txtExportFile.Text For Append As #1
    
    Print #1, ""
    Print #1, ""
    Print #1, ""
    Print #1, "## LIIK ##"
    Print #1, ""
    
    gRS.Open "SELECT DISTINCT TRIM(NIMI) AS NIMI FROM liik ORDER BY TRIM(NIMI)", gConnect
    Do Until gRS.EOF
        
        myString = ""
        myString = myString & "INSERT IGNORE INTO tags SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldNumber("tagtype_id", 3)
        myString = myString & FieldString("name", gRS("NIMI"))
        myString = myString & ";"
        
        Print #1, myString
        gRS.MoveNext
    Loop
    gRS.Close

    Print #1, ""
    Print #1, ""
    Print #1, ""
    
    If chkDeleteRows.Value = vbChecked Then Print #1, "DELETE FROM media_tags WHERE old_id LIKE '" & txtLibraryID.Text & "-%' AND tag_id IN (SELECT id FROM tags WHERE tagtype_id = 3);"

    gRS.Open "SELECT MEEDIA_ID, TRIM(NIMI) AS NIMI FROM meedia, liik WHERE LIIK_FK = LIIK_ID AND LEN(TRIM(NIMI))>0 ORDER BY MEEDIA_ID", gConnect
    Do Until gRS.EOF

        myString = ""
        myString = myString & "INSERT INTO media_tags SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldString("old_id", txtLibraryID.Text & "-")
        myString = myString & FieldSelect("media", "media_id", gRS("MEEDIA_ID"))
        myString = myString & ", tag_id = (SELECT id FROM tags WHERE UPPER(TRIM(name)) = '" & UCase(gRS("NIMI")) & "' and tagtype_id = 3 LIMIT 0, 1)"
        myString = myString & ";"

        Print #1, myString

        gRS.MoveNext
    Loop
    gRS.Close

    Close #1

End Sub

Private Sub Export_Marksona()
    Dim myString As String
    
    Open txtExportFile.Text For Append As #1
    
    Print #1, ""
    Print #1, ""
    Print #1, ""
    Print #1, "## MARKSONA ##"
    Print #1, ""
    
    gRS.Open "SELECT DISTINCT TRIM(NIMI) AS NIMI FROM marksona ORDER BY TRIM(NIMI)", gConnect
    Do Until gRS.EOF
        
        myString = ""
        myString = myString & "INSERT IGNORE INTO tags SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldNumber("tagtype_id", 4)
        myString = myString & FieldString("name", gRS("NIMI"))
        myString = myString & ";"
        
        Print #1, myString
        gRS.MoveNext
    Loop
    gRS.Close

    Print #1, ""
    Print #1, ""
    Print #1, ""
    
    If chkDeleteRows.Value = vbChecked Then Print #1, "DELETE FROM media_tags WHERE old_id LIKE '" & txtLibraryID.Text & "-%' AND tag_id IN (SELECT id FROM tags WHERE tagtype_id = 4);"

    gRS.Open "SELECT MEEDIA_FK, TRIM(NIMI) AS NIMI FROM meedia_marksona, marksona WHERE marksona_fk = marksona_id AND LEN(TRIM(NIMI))>0 ORDER BY MEEDIA_fk", gConnect
    Do Until gRS.EOF

        myString = ""
        myString = myString & "INSERT INTO media_tags SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldString("old_id", txtLibraryID.Text & "-")
        myString = myString & FieldSelect("media", "media_id", gRS("MEEDIA_fk"))
        myString = myString & ", tag_id = (SELECT id FROM tags WHERE UPPER(TRIM(name)) = '" & UCase(gRS("NIMI")) & "' and tagtype_id = 4 LIMIT 0, 1)"
        myString = myString & ";"

        Print #1, myString

        gRS.MoveNext
    Loop
    gRS.Close

    Close #1

End Sub

Private Sub Export_Valjaandja()
    Dim myString As String
    
    Open txtExportFile.Text For Append As #1
    
    Print #1, ""
    Print #1, ""
    Print #1, ""
    Print #1, "## VALJAANDJA ##"
    Print #1, ""
    
    gRS.Open "SELECT DISTINCT TRIM(NIMI) AS NIMI FROM valjaandja ORDER BY TRIM(NIMI)", gConnect
    Do Until gRS.EOF
        
        myString = ""
        myString = myString & "INSERT IGNORE INTO tags SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldNumber("tagtype_id", 5)
        myString = myString & FieldString("name", gRS("NIMI"))
        myString = myString & ";"
        
        Print #1, myString
        gRS.MoveNext
    Loop
    gRS.Close

    Print #1, ""
    Print #1, ""
    Print #1, ""
    
    If chkDeleteRows.Value = vbChecked Then Print #1, "DELETE FROM media_tags WHERE old_id LIKE '" & txtLibraryID.Text & "-%' AND tag_id IN (SELECT id FROM tags WHERE tagtype_id = 5);"

    gRS.Open "SELECT MEEDIA_ID, TRIM(NIMI) AS NIMI FROM meedia, valjaandja WHERE valjaandja_FK = valjaandja_ID AND LEN(TRIM(NIMI))>0 ORDER BY MEEDIA_ID", gConnect
    Do Until gRS.EOF

        myString = ""
        myString = myString & "INSERT INTO media_tags SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldString("old_id", txtLibraryID.Text & "-")
        myString = myString & FieldSelect("media", "media_id", gRS("MEEDIA_ID"))
        myString = myString & ", tag_id = (SELECT id FROM tags WHERE UPPER(TRIM(name)) = '" & UCase(gRS("NIMI")) & "' and tagtype_id = 5 LIMIT 0, 1)"
        myString = myString & ";"

        Print #1, myString

        gRS.MoveNext
    Loop
    gRS.Close

    Close #1
    
End Sub

Private Sub Export_Meedia_Field(ByVal sField As String, ByVal sTagTypeID As String)
    Dim myString As String
    
    Open txtExportFile.Text For Append As #1
    
    Print #1, ""
    Print #1, ""
    Print #1, ""
    Print #1, "## MEEDIA " & UCase(sField) & " ##"
    Print #1, ""
    
    gRS.Open "SELECT DISTINCT TRIM(" & sField & ") AS NIMI FROM meedia WHERE LEN(" & sField & ") > 0 ORDER BY TRIM(" & sField & ")", gConnect
    Do Until gRS.EOF
        
        myString = ""
        myString = myString & "INSERT IGNORE INTO tags SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldNumber("tagtype_id", sTagTypeID)
        myString = myString & FieldString("name", gRS("NIMI"))
        myString = myString & ";"

        Print #1, myString
        gRS.MoveNext
    Loop
    gRS.Close

    Print #1, ""
    Print #1, ""
    Print #1, ""
    
    If chkDeleteRows.Value = vbChecked Then Print #1, "DELETE FROM media_tags WHERE old_id LIKE '" & txtLibraryID.Text & "-%' AND tag_id IN (SELECT id FROM tags WHERE tagtype_id = " & sTagTypeID & ");"

    gRS.Open "SELECT MEEDIA_ID, TRIM(" & sField & ") AS NIMI FROM meedia WHERE LEN(TRIM(" & sField & "))>0 ORDER BY MEEDIA_ID", gConnect
    Do Until gRS.EOF

        myString = ""
        myString = myString & "INSERT INTO media_tags SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldString("old_id", txtLibraryID.Text & "-")
        myString = myString & FieldSelect("media", "media_id", gRS("MEEDIA_ID"))
        myString = myString & ", tag_id = (SELECT id FROM tags WHERE UPPER(TRIM(name)) = '" & UCase(gRS("NIMI")) & "' and tagtype_id = " & sTagTypeID & " LIMIT 0, 1)"
        myString = myString & ";"

        Print #1, myString

        gRS.MoveNext
    Loop
    gRS.Close

    Close #1
    
End Sub







Private Sub Export_Autor()
    Dim myString As String
    
    Open txtExportFile.Text For Append As #1
    
    Print #1, ""
    Print #1, ""
    Print #1, ""
    Print #1, "## AUTOR ##"
    Print #1, ""
    
    gRS.Open "SELECT * FROM autor ORDER BY NIMI, EESNIMI", gConnect
    Do Until gRS.EOF

        myString = ""
        myString = myString & "INSERT IGNORE INTO persons SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldString("firstname", gRS("EESNIMI"))
        myString = myString & FieldString("lastname", gRS("NIMI"))
        myString = myString & FieldString("nationality", gRS("RAHVUS"))
        myString = myString & FieldString("note", IIf(Len(Trim(gRS("ELUAASTAD"))) > 0, Trim(gRS("ELUAASTAD")) & vbCrLf & vbCrLf, "") & Trim(gRS("MARKUSED")))
        myString = myString & ";"

        Print #1, myString
        gRS.MoveNext
    Loop
    gRS.Close

    Print #1, ""
    Print #1, ""
    Print #1, ""

    If chkDeleteRows.Value = vbChecked Then Print #1, "DELETE FROM media_persons WHERE old_id LIKE '" & txtLibraryID.Text & "-%';"

    gRS.Open "SELECT MEEDIA_fk, TRIM(EESNIMI) & TRIM(NIMI) AS NIMI FROM meedia_autor, autor WHERE autor_FK = autor_ID AND LEN(TRIM(EESNIMI) & TRIM(NIMI))>0 ORDER BY MEEDIA_fk", gConnect
    Do Until gRS.EOF

        myString = ""
        myString = myString & "INSERT INTO media_persons SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldString("old_id", txtLibraryID.Text & "-")
        myString = myString & FieldNumber("tagtype_id", 9)
        myString = myString & FieldSelect("media", "media_id", gRS("MEEDIA_fk"))
        myString = myString & ", person_id = (SELECT id FROM persons WHERE UPPER(CONCAT(TRIM(firstname),TRIM(lastname))) = '" & UCase(gRS("NIMI")) & "' LIMIT 0, 1)"
        myString = myString & ";"

        Print #1, myString

        gRS.MoveNext
    Loop
    gRS.Close

    Close #1

End Sub







Private Sub Export_MeediaEksemplar()
    Dim myString As String
    
    Open txtExportFile.Text For Append As #1
    
    Print #1, ""
    Print #1, ""
    Print #1, ""
    Print #1, "## EKSEMPLAR ##"
    Print #1, ""
    If chkDeleteRows.Value = vbChecked Then Print #1, "DELETE FROM items WHERE old_id LIKE '" & txtLibraryID.Text & "-%';"
    
    gRS.Open "SELECT * FROM meedia_eksemplar", gConnect
    Do Until gRS.EOF
        
        myString = ""
        myString = myString & "INSERT INTO items SET "
        myString = myString & "created_time = NOW()"
        myString = myString & FieldString("old_id", txtLibraryID.Text & "-" & gRS("MEEDIA_EKSEMPLAR_ID"))
        myString = myString & FieldString("library_id", txtLibraryID.Text)
        myString = myString & FieldSelect("media", "media_id", gRS("MEEDIA_FK"))
        myString = myString & FieldNumber("item_number", gRS("INVENTARI_NUMBER"))
       ' myString = myString & FieldString("number_perioodika", gRS("NUMBER"))
       ' myString = myString & FieldDate("kpv_sisse", gRS("SISSEKANDE_KUUPAEV"))
       ' myString = myString & FieldSelect("saatedokument", "saatedokument_fk", gRS("SAATEDOKUMENT_FK"))
       ' myString = myString & FieldSelect("mahakandmisakt", "mahakandmisakt_fk", gRS("MAHAKANDMISAKT_FK"))
        myString = myString & FieldNumber("quantity", gRS("KOGUS"))
        myString = myString & FieldNumber("price", gRS("HIND"))
        myString = myString & FieldString("note", gRS("MARKUSED"))
        myString = myString & ";"
        
        Print #1, myString
        gRS.MoveNext
    Loop
    gRS.Close
    
    Close #1

End Sub







Private Sub Export_Mahakandmisakt()
    Dim myString As String

    Open txtExportFile.Text For Append As #1

    Print #1, ""
    Print #1, ""
    Print #1, ""
    Print #1, "## MAHAKANDMISAKT ##"
    Print #1, ""
    If chkDeleteRows.Value = vbChecked Then Print #1, "DELETE FROM mahakandmisakt WHERE old_id LIKE '" & txtLibraryID.Text & "-%';"

    gRS.Open "SELECT * FROM mahakandmisakt", gConnect
    Do Until gRS.EOF

        myString = ""
        myString = myString & "INSERT INTO mahakandmisakt SET "
        myString = myString & "library_id = " & txtLibraryID.Text
        myString = myString & FieldNumber("old_id", gRS("MAHAKANDMISAKT_ID"))
        myString = myString & FieldString("meedia_liik", gRS("MEEDIA_LIIK"))
        myString = myString & FieldString("number", gRS("AKTI_NUMBER"))
        myString = myString & FieldString("pohjus", gRS("POHJUS"))
        myString = myString & FieldString("kpv", Format(gRS("KUUPAEV"), "YYYY-MM-DD HH:NN:SS"))
        myString = myString & ";"

        Print #1, myString
        gRS.MoveNext
    Loop
    gRS.Close

    Close #1

End Sub

Private Sub Export_Saatedokument()
    Dim myString As String
    
    Close #1
    Open txtExportFile.Text For Append As #1
    
    Print #1, ""
    Print #1, ""
    Print #1, ""
    Print #1, "## SAATEDOKUMENT ##"
    Print #1, ""
    If chkDeleteRows.Value = vbChecked Then Print #1, "DELETE FROM saatedokument WHERE old_id LIKE '" & txtLibraryID.Text & "-%';"
    
    gRS.Open "SELECT * FROM saatedokument", gConnect
    Do Until gRS.EOF
        
        myString = ""
        myString = myString & "INSERT INTO saatedokument SET "
        myString = myString & "library_id = " & txtLibraryID.Text
        myString = myString & FieldNumber("old_id", gRS("SAATEDOKUMENT_ID"))
        myString = myString & FieldString("number", gRS("DOKUMENDI_NUMBER"))
        myString = myString & FieldString("kpv", Format(gRS("KUUPAEV"), "YYYY-MM-DD HH:NN:SS"))
        myString = myString & FieldSelect("valjaandja", "valjaandja_fk", gRS("VALJAANDJA_FK"))
        myString = myString & FieldString("note", gRS("MARKUSED"))
        myString = myString & ";"
        
        Print #1, myString
        
        gRS.MoveNext
    Loop
    gRS.Close
    
    Close #1

End Sub







Private Function getMaakond(ByVal sMaakondID)
    Dim myVastus As String
    Dim myRS As ADODB.Recordset
    
    myVastus = ""
    
    If IsNumeric(sMaakondID) Then
        Set myRS = New ADODB.Recordset
        myRS.Open "SELECT NIMI FROM maakond WHERE MAAKOND_ID = " & sMaakondID, gConnect
        myVastus = myRS("NIMI")
        myRS.Close
    End If

    getMaakond = myVastus
    
End Function







Private Function FieldString(ByVal sField As String, ByVal sValue) As String
    Dim myVastus As String
    
    myVastus = ""

    sValue = Trim(sValue)
    If Len(sValue) > 0 Then
        myVastus = ", " & sField & " = '" & Replace(sValue & "", "'", "\'") & "'"
    End If

    FieldString = myVastus
    
End Function

Private Function FieldNumber(ByVal sField As String, ByVal sValue) As String
    Dim myVastus As String
    
    myVastus = ""
    
    sValue = Trim(sValue)
    If Len(sValue) > 0 Then
        myVastus = ", " & sField & " = " & Replace(sValue & "", ",", ".")
    End If

    FieldNumber = myVastus
    
End Function

Private Function FieldDate(ByVal sField As String, ByVal sValue) As String
    Dim myVastus As String
    
    myVastus = ""
    
    If IsDate(sValue) = True Then
        myVastus = ", " & sField & " = '" & Format(sValue, "yyyy-mm-dd Hh:Nn:Ss") & "'"
    End If

    FieldDate = myVastus
    
End Function

Private Function FieldSelect(ByVal sTable As String, ByVal sField As String, ByVal sValue) As String
    Dim myVastus As String
    
    myVastus = ""
    
    If IsNumeric(sValue) = True Then
        If sValue > 0 Then
            myVastus = ", " & sField & " = "
            myVastus = myVastus & "(SELECT id FROM " & sTable & " WHERE old_id = '" & txtLibraryID.Text & "-" & sValue & "' LIMIT 0, 1)"
        End If
    End If

    FieldSelect = myVastus
    
End Function
