VERSION 5.00
Object = "{F9043C88-F6F2-101A-A3C9-08002B2F49FB}#1.2#0"; "COMDLG32.OCX"
Object = "{48E59290-9880-11CF-9754-00AA00C00908}#1.0#0"; "MSINET.OCX"
Begin VB.Form Form1 
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Form1"
   ClientHeight    =   4470
   ClientLeft      =   45
   ClientTop       =   360
   ClientWidth     =   5610
   BeginProperty Font 
      Name            =   "Verdana"
      Size            =   9
      Charset         =   186
      Weight          =   400
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   Icon            =   "ARX2Entu.frx":0000
   LinkTopic       =   "Form1"
   LockControls    =   -1  'True
   MaxButton       =   0   'False
   MinButton       =   0   'False
   ScaleHeight     =   4470
   ScaleWidth      =   5610
   StartUpPosition =   3  'Windows Default
   Begin InetCtlsObjects.Inet Inet1 
      Left            =   3255
      Top             =   105
      _ExtentX        =   1005
      _ExtentY        =   1005
      _Version        =   393216
   End
   Begin VB.CheckBox chkSaatedokument 
      Caption         =   "saatedokumendid"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   225
      Left            =   210
      TabIndex        =   13
      Top             =   3675
      Value           =   1  'Checked
      Width           =   2220
   End
   Begin VB.CheckBox chkLugeja 
      Caption         =   "lugejad"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   225
      Left            =   210
      TabIndex        =   12
      Top             =   3045
      Value           =   1  'Checked
      Width           =   2220
   End
   Begin VB.CheckBox chkMeedia 
      Caption         =   "teavikud"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   225
      Left            =   210
      TabIndex        =   11
      Top             =   3360
      Value           =   1  'Checked
      Width           =   2220
   End
   Begin VB.CheckBox chkLaenutus 
      Caption         =   "laenutused"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   225
      Left            =   210
      TabIndex        =   10
      Top             =   3990
      Value           =   1  'Checked
      Width           =   2220
   End
   Begin MSComDlg.CommonDialog FileAccess 
      Left            =   2625
      Top             =   105
      _ExtentX        =   847
      _ExtentY        =   847
      _Version        =   393216
   End
   Begin VB.TextBox txtDatabaseFile 
      Appearance      =   0  'Flat
      BackColor       =   &H8000000F&
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
      Height          =   330
      Left            =   210
      Locked          =   -1  'True
      TabIndex        =   7
      TabStop         =   0   'False
      Top             =   1050
      Width           =   5160
   End
   Begin VB.TextBox txtLibraryName 
      Appearance      =   0  'Flat
      BackColor       =   &H8000000F&
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
      Height          =   330
      Left            =   210
      Locked          =   -1  'True
      TabIndex        =   5
      TabStop         =   0   'False
      Top             =   420
      Width           =   5160
   End
   Begin VB.TextBox txtExportFile 
      Appearance      =   0  'Flat
      BackColor       =   &H8000000F&
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
      Height          =   330
      Left            =   210
      Locked          =   -1  'True
      TabIndex        =   3
      TabStop         =   0   'False
      Top             =   1680
      Width           =   5160
   End
   Begin VB.CommandButton btnExport 
      Caption         =   "Ekspordi andmed SQL faili"
      Default         =   -1  'True
      Enabled         =   0   'False
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   540
      Left            =   3255
      TabIndex        =   2
      Top             =   3675
      Width           =   2115
   End
   Begin VB.TextBox txtDatabase 
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   186
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   330
      Left            =   210
      TabIndex        =   1
      Top             =   2310
      Width           =   5160
   End
   Begin VB.Label Label5 
      Appearance      =   0  'Flat
      AutoSize        =   -1  'True
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "Ekspordi:"
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
      Height          =   195
      Left            =   210
      TabIndex        =   9
      Top             =   2835
      Width           =   915
   End
   Begin VB.Shape shpProgress 
      BackColor       =   &H8000000D&
      BackStyle       =   1  'Opaque
      BorderStyle     =   0  'Transparent
      FillColor       =   &H80000008&
      Height          =   225
      Left            =   0
      Top             =   4410
      Width           =   330
   End
   Begin VB.Label Label4 
      Appearance      =   0  'Flat
      AutoSize        =   -1  'True
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "ARX-Raamat v7 fail:"
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
      Height          =   195
      Left            =   210
      TabIndex        =   8
      Top             =   840
      Width           =   1935
   End
   Begin VB.Label Label3 
      Appearance      =   0  'Flat
      AutoSize        =   -1  'True
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "Raamatukogu:"
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
      Height          =   195
      Left            =   210
      TabIndex        =   6
      Top             =   210
      Width           =   1395
   End
   Begin VB.Label Label2 
      Appearance      =   0  'Flat
      AutoSize        =   -1  'True
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "SQL fail:"
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
      Height          =   195
      Left            =   210
      TabIndex        =   4
      Top             =   1470
      Width           =   795
   End
   Begin VB.Label Label1 
      Appearance      =   0  'Flat
      AutoSize        =   -1  'True
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "Entu andmebaas:"
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
      Height          =   195
      Left            =   210
      TabIndex        =   0
      Top             =   2100
      Width           =   1680
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Dim gConnect As ADODB.Connection
Dim gRS As ADODB.Recordset
Dim gCount As Long
Dim gStep As Long

Private Sub Form_Activate()
    txtDatabase.SetFocus
End Sub

Private Sub Form_Load()
    Me.Caption = App.ProductName & " - " & App.Major & "." & App.Minor & "." & App.Revision

    FileAccess.CancelError = False
    FileAccess.Filter = "ARX-Raamat Database File|*.mdb"
    FileAccess.ShowOpen

    If LenB(FileAccess.FileName) = 0 Then
        End
    Else
        shpProgress.Width = 0
        gCount = 0
        gStep = 0
        
        txtDatabaseFile.Text = FileAccess.FileName
        txtExportFile.Text = Left(FileAccess.FileName, Len(FileAccess.FileName) - 4) & "2Entu.sql"
        
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

Private Sub txtDatabase_Change()
    If txtDatabase.Text <> Trim(txtDatabase.Text) Then
        txtDatabase.Text = Trim(txtDatabase.Text)
        txtDatabase.SelStart = Len(txtDatabase.Text)
    End If
    If Len(txtDatabase.Text) > 0 Then
        btnExport.Enabled = True
    Else
        btnExport.Enabled = False
    End If
End Sub

Private Sub txtDatabase_GotFocus()
    txtDatabase.SelStart = 0
    txtDatabase.SelLength = Len(txtDatabase.Text)
End Sub

Private Sub btnExport_Click()
    Dim myFilename As String
    
    Screen.MousePointer = vbHourglass
    txtDatabase.Enabled = False
    btnExport.Enabled = False
    
    Open txtExportFile.Text For Output As #1
    Print #1, "## Database:       " & txtDatabase.Text
    Print #1, "## Library name:   " & txtLibraryName.Text
    Print #1, "## Export started: " & Format(Now, "yyyy-mm-dd Hh:Nn:Ss")
    Close #1
    
    Open Replace(txtExportFile.Text, ".sql", ".rus.sql") For Output As #1
    Print #1, "## Database:       " & txtDatabase.Text
    Print #1, "## Library name:   " & txtLibraryName.Text
    Print #1, "## Export started: " & Format(Now, "yyyy-mm-dd Hh:Nn:Ss")
    Close #1
    
    chkLugeja.Enabled = False
    If chkLugeja.Value = vbChecked Then
        Export_Klass
        Export_Lugeja
    End If

    chkMeedia.Enabled = False
    If chkMeedia.Value = vbChecked Then
        Export_Meedia
        Export_MeediaAutor
        Export_MeediaMarksona
        Export_MeediaEksemplar
    End If
    
    chkLaenutus.Enabled = False
    If chkLaenutus.Value = vbChecked Then
        Export_Laenutus
    End If
    
    Open txtExportFile.Text For Append As #1
    Print #1, ""
    Print #1, ""
    Print #1, "## Database:     " & txtDatabase.Text
    Print #1, "## Library name: " & txtLibraryName.Text
    Print #1, "## Export ended: " & Format(Now, "yyyy-mm-dd Hh:Nn:Ss")
    Print #1, ""
    Print #1, ""
    Print #1, "## END "
    Close #1
    
    Open Replace(txtExportFile.Text, ".sql", ".rus.sql") For Append As #1
    Print #1, ""
    Print #1, ""
    Print #1, "## Database:     " & txtDatabase.Text
    Print #1, "## Library name: " & txtLibraryName.Text
    Print #1, "## Export ended: " & Format(Now, "yyyy-mm-dd Hh:Nn:Ss")
    Print #1, ""
    Print #1, ""
    Print #1, "## END "
    Close #1
    
    Screen.MousePointer = vbDefault
    
    MsgBox FileAccess.FileName & " exported to " & txtExportFile.Text, vbInformation
    
    End
    
End Sub

Private Sub moveProgress()
    gStep = gStep + 1
    shpProgress.Width = Me.Width / gCount * gStep
    DoEvents
End Sub

Private Sub Export_Klass()

    Open txtExportFile.Text For Append As #1
    Print #1, ""
    Print #1, ""
    Print #1, "## KLASS"
    Close #1
    
    gRS.Open "SELECT KLASS_ID, KLASSI_NUMBER, KLASSI_TAHT, MARKUSED " _
           & "FROM klass " _
           & "ORDER BY KLASSI_NUMBER, KLASSI_TAHT;", gConnect
    Do Until gRS.EOF
        gCount = gCount + 1
        gRS.MoveNext
    Loop
    If gRS.BOF = False Then
        gRS.MoveFirst
    End If
    deleteChild "klassilugeja-"
    deleteEntity "klass-"
    Do Until gRS.EOF
        createEntity "klass-" & gRS("KLASS_ID"), "class"
        createProperty "klass-" & gRS("KLASS_ID"), "integer", "class-number", gRS("KLASSI_NUMBER")
        createProperty "klass-" & gRS("KLASS_ID"), "string", "class-letter", gRS("KLASSI_TAHT")
        createProperty "klass-" & gRS("KLASS_ID"), "string", "class-notes", gRS("MARKUSED")
        gRS.MoveNext
        moveProgress
    Loop
    
    gRS.Close
    
End Sub

Private Sub Export_Lugeja()

    Open txtExportFile.Text For Append As #1
    Print #1, ""
    Print #1, ""
    Print #1, "## LUGEJA"
    Close #1
    
    gRS.Open "SELECT LUGEJA_ID, KLASS_FK, EESNIMI, lugeja.NIMI, AADRESS, LINN, maakond.NIMI AS MAAKOND, POSTIINDEKS, TELEFON, MARKUSED " _
           & "FROM lugeja " _
           & "LEFT JOIN maakond ON lugeja.MAAKOND_FK = maakond.MAAKOND_ID " _
           & "ORDER BY lugeja.NIMI, EESNIMI;", gConnect
    Do Until gRS.EOF
        gCount = gCount + 1
        gRS.MoveNext
    Loop
    If gRS.BOF = False Then
        gRS.MoveFirst
    End If
    deleteEntity "lugeja-"
    Do Until gRS.EOF
        createEntity "lugeja-" & gRS("LUGEJA_ID"), "person"
        createProperty "lugeja-" & gRS("LUGEJA_ID"), "string", "person-forename", gRS("EESNIMI")
        createProperty "lugeja-" & gRS("LUGEJA_ID"), "string", "person-surname", gRS("NIMI")
        createProperty "lugeja-" & gRS("LUGEJA_ID"), "string", "person-address", gRS("AADRESS")
        createProperty "lugeja-" & gRS("LUGEJA_ID"), "string", "person-town", gRS("LINN")
        createProperty "lugeja-" & gRS("LUGEJA_ID"), "string", "person-county", gRS("MAAKOND")
        createProperty "lugeja-" & gRS("LUGEJA_ID"), "string", "person-postalcode", gRS("POSTIINDEKS")
        createProperty "lugeja-" & gRS("LUGEJA_ID"), "string", "person-phone", gRS("TELEFON")
        createProperty "lugeja-" & gRS("LUGEJA_ID"), "string", "person-notes", gRS("MARKUSED")
        createChild "klassilugeja-" & gRS("KLASS_FK") & "-" & gRS("LUGEJA_ID"), "klass-" & gRS("KLASS_FK"), "lugeja-" & gRS("LUGEJA_ID")
        gRS.MoveNext
        moveProgress
    Loop
    
    gRS.Close

End Sub

Private Sub Export_Meedia()
    Dim myType As String
    Dim myText As String
    
    Open txtExportFile.Text For Append As #1
    Print #1, ""
    Print #1, ""
    Print #1, "## MEEDIA"
    Close #1

    gRS.Open "SELECT MEEDIA_ID, MEEDIA_LIIK, PEALKIRI, KLASS, andmekandja.NIMI AS ANDMEKANDJA, ILMUMISAASTA, liik.NIMI AS LIIK, keel.NIMI AS KEEL, valjaandja.NIMI AS VALJAANDJA, RIIUL, meedia.MARKUSED " _
           & "FROM (((meedia " _
           & "LEFT JOIN andmekandja ON meedia.ANDMEKANDJA_FK = andmekandja.ANDMEKANDJA_ID) " _
           & "LEFT JOIN liik ON meedia.LIIK_FK = liik.LIIK_ID) " _
           & "LEFT JOIN keel ON meedia.KEEL_FK = keel.KEEL_ID) " _
           & "LEFT JOIN valjaandja ON meedia.VALJAANDJA_FK = valjaandja.VALJAANDJA_ID " _
           & "ORDER BY MEEDIA_LIIK, PEALKIRI;", gConnect
    Do Until gRS.EOF
        gCount = gCount + 1
        gRS.MoveNext
    Loop
    If gRS.BOF = False Then
        gRS.MoveFirst
    End If
    deleteEntity "meedia-"
    Do Until gRS.EOF
        Select Case gRS("MEEDIA_LIIK")
            Case "RA"
                myType = "book"
            Case "OP"
                myType = "textbook"
            Case "TV"
                myType = "workbook"
            Case "PE"
                myType = "periodical"
            Case "AV"
                myType = "audiovideo"
            Case "MK"
                myType = "methodical"
        End Select
        
        createEntity "meedia-" & gRS("MEEDIA_ID"), myType
        createProperty "meedia-" & gRS("MEEDIA_ID"), "string", myType & "-title", gRS("PEALKIRI")
        createProperty "meedia-" & gRS("MEEDIA_ID"), "string", myType & "-class", gRS("KLASS")
        createProperty "meedia-" & gRS("MEEDIA_ID"), "string", myType & "-media", gRS("ANDMEKANDJA")
        createProperty "meedia-" & gRS("MEEDIA_ID"), "string", myType & "-publishing-date", gRS("ILMUMISAASTA")
        createProperty "meedia-" & gRS("MEEDIA_ID"), "string", myType & "-udc", gRS("LIIK")
        createProperty "meedia-" & gRS("MEEDIA_ID"), "string", myType & "-language", gRS("KEEL")
        createProperty "meedia-" & gRS("MEEDIA_ID"), "string", myType & "-publisher", gRS("VALJAANDJA")
        createProperty "meedia-" & gRS("MEEDIA_ID"), "string", myType & "-location", gRS("RIIUL")
        createProperty "meedia-" & gRS("MEEDIA_ID"), "string", myType & "-notes", gRS("MARKUSED")
        gRS.MoveNext
        moveProgress
    Loop
    gRS.Close
    
End Sub

Private Sub Export_MeediaAutor()
    Dim myType As String
    Dim myText As String
    
    Open txtExportFile.Text For Append As #1
    Print #1, ""
    Print #1, ""
    Print #1, "## MEEDIA_AUTOR"
    Close #1

    gRS.Open "SELECT DISTINCT MEEDIA.MEEDIA_ID, MEEDIA.MEEDIA_LIIK, AUTOR.NIMI, AUTOR.EESNIMI " _
           & "FROM (MEEDIA_AUTOR " _
           & "LEFT JOIN AUTOR ON MEEDIA_AUTOR.AUTOR_FK = AUTOR.AUTOR_ID) " _
           & "RIGHT JOIN MEEDIA ON MEEDIA_AUTOR.MEEDIA_FK = MEEDIA.MEEDIA_ID " _
           & "WHERE AUTOR.AUTOR_ID Is Not Null " _
           & "ORDER BY MEEDIA.MEEDIA_ID, AUTOR.NIMI, AUTOR.EESNIMI;", gConnect
    Do Until gRS.EOF
        gCount = gCount + 1
        gRS.MoveNext
    Loop
    If gRS.BOF = False Then
        gRS.MoveFirst
    End If
    Do Until gRS.EOF
        Select Case gRS("MEEDIA_LIIK")
            Case "RA"
                myType = "book"
            Case "OP"
                myType = "textbook"
            Case "TV"
                myType = "workbook"
            Case "PE"
                myType = "periodical"
            Case "AV"
                myType = "audiovideo"
            Case "MK"
                myType = "methodical"
        End Select
        
        myText = ""
        If Len(Trim(gRS("NIMI"))) > 0 Then
            myText = Trim(gRS("NIMI"))
        End If
        If Len(myText) > 0 And Len(Trim(gRS("EESNIMI"))) > 0 Then
            myText = myText & ", "
        End If
        If Len(Trim(gRS("EESNIMI"))) Then
            myText = myText & Trim(gRS("EESNIMI"))
        End If
        
        createProperty "meedia-" & gRS("MEEDIA_ID"), "string", myType & "-author", myText
        gRS.MoveNext
        moveProgress
    Loop
    gRS.Close
    
End Sub

Private Sub Export_MeediaMarksona()
    Dim myType As String
    
    Open txtExportFile.Text For Append As #1
    Print #1, ""
    Print #1, ""
    Print #1, "## MEEDIA_MARKSONA"
    Close #1

    gRS.Open "SELECT DISTINCT MEEDIA.MEEDIA_ID, MEEDIA.MEEDIA_LIIK, MARKSONA.NIMI " _
           & "FROM (MEEDIA_MARKSONA " _
           & "LEFT JOIN MARKSONA ON MEEDIA_MARKSONA.MARKSONA_FK = MARKSONA.MARKSONA_ID) " _
           & "RIGHT JOIN MEEDIA ON MEEDIA_MARKSONA.MEEDIA_FK = MEEDIA.MEEDIA_ID " _
           & "WHERE MARKSONA.MARKSONA_ID Is Not Null " _
           & "ORDER BY MEEDIA.MEEDIA_ID, MARKSONA.NIMI;", gConnect
    Do Until gRS.EOF
        gCount = gCount + 1
        gRS.MoveNext
    Loop
    If gRS.BOF = False Then
        gRS.MoveFirst
    End If
    Do Until gRS.EOF
        Select Case gRS("MEEDIA_LIIK")
            Case "RA"
                myType = "book"
            Case "OP"
                myType = "textbook"
            Case "TV"
                myType = "workbook"
            Case "PE"
                myType = "periodical"
            Case "AV"
                myType = "audiovideo"
            Case "MK"
                myType = "methodical"
        End Select
        
        createProperty "meedia-" & gRS("MEEDIA_ID"), "string", myType & "-tag", gRS("NIMI")
        gRS.MoveNext
        moveProgress
    Loop
    gRS.Close
    
End Sub

Private Sub Export_MeediaEksemplar()
    Dim myN As Integer
    
    Open txtExportFile.Text For Append As #1
    Print #1, ""
    Print #1, ""
    Print #1, "## MEEDIA_EKSEMPLAR"
    Close #1

    gRS.Open "SELECT MEEDIA_EKSEMPLAR_ID, MEEDIA.MEEDIA_ID, MEEDIA_EKSEMPLAR.INVENTARI_NUMBER, MEEDIA_EKSEMPLAR.SISSEKANDE_KUUPAEV, MEEDIA_EKSEMPLAR.HIND, MEEDIA_EKSEMPLAR.KOGUS - IIF(MEEDIA_EKSEMPLAR.MYYDUD_KOGUS > 0, MEEDIA_EKSEMPLAR.MYYDUD_KOGUS, 0) AS KOGUS, MEEDIA_EKSEMPLAR.NUMBER, MEEDIA_EKSEMPLAR.MARKUSED " _
           & "FROM MEEDIA " _
           & "LEFT JOIN MEEDIA_EKSEMPLAR ON MEEDIA.MEEDIA_ID = MEEDIA_EKSEMPLAR.MEEDIA_FK " _
           & "WHERE MEEDIA_EKSEMPLAR.MEEDIA_EKSEMPLAR_ID Is Not Null AND MEEDIA_EKSEMPLAR.MAHAKANDMISAKT_FK = 0 " _
           & "ORDER BY MEEDIA.MEEDIA_ID;", gConnect
    Do Until gRS.EOF
        gCount = gCount + 1
        gRS.MoveNext
    Loop
    If gRS.BOF = False Then
        gRS.MoveFirst
    End If
    deleteChild "meediaeksemplar-"
    deleteEntity "eksemplar-"
    Do Until gRS.EOF
        For myN = 1 To gRS("KOGUS")
            createEntity "eksemplar-" & gRS("MEEDIA_EKSEMPLAR_ID") & "-" & myN, "copy"
            createProperty "eksemplar-" & gRS("MEEDIA_EKSEMPLAR_ID") & "-" & myN, "string", "copy-inventory-number", gRS("INVENTARI_NUMBER")
            createProperty "eksemplar-" & gRS("MEEDIA_EKSEMPLAR_ID") & "-" & myN, "date", "copy-date-added", gRS("SISSEKANDE_KUUPAEV")
            createProperty "eksemplar-" & gRS("MEEDIA_EKSEMPLAR_ID") & "-" & myN, "decimal", "copy-price", gRS("HIND")
            createProperty "eksemplar-" & gRS("MEEDIA_EKSEMPLAR_ID") & "-" & myN, "string", "copy-number", gRS("NUMBER")
            createProperty "eksemplar-" & gRS("MEEDIA_EKSEMPLAR_ID") & "-" & myN, "string", "copy-notes", gRS("MARKUSED")
            createChild "meediaeksemplar-" & gRS("MEEDIA_ID") & "-" & gRS("MEEDIA_EKSEMPLAR_ID") & "-" & myN, "meedia-" & gRS("MEEDIA_ID"), "eksemplar-" & gRS("MEEDIA_EKSEMPLAR_ID") & "-" & myN
        Next
        gRS.MoveNext
        moveProgress
    Loop
    gRS.Close
    
End Sub

Private Sub Export_Laenutus()

    Open txtExportFile.Text For Append As #1
    Print #1, ""
    Print #1, ""
    Print #1, "## LAENUTUS"
    Close #1
    
    gRS.Open "SELECT LAENUTUS_ID, LUGEJA_FK, MEEDIA_FK, MEEDIA_EKSEMPLAR_FK, LAENUTUS_KUUPAEV, TAHTAEG_KUUPAEV, TAGASTUS_KUUPAEV " _
           & "FROM laenutus " _
           & "WHERE MEEDIA_LIIK IN ('RA', 'AV', 'PE') " _
           & "ORDER BY LAENUTUS_ID;", gConnect
    Do Until gRS.EOF
        gCount = gCount + 1
        gRS.MoveNext
    Loop
    If gRS.BOF = False Then
        gRS.MoveFirst
    End If
    deleteEntity "laenutus-"
    Do Until gRS.EOF
        createEntity "laenutus-" & gRS("LAENUTUS_ID"), "lending"
        createProperty "laenutus-" & gRS("LAENUTUS_ID"), "reference", "lending-person", "lugeja-" & gRS("LUGEJA_FK")
        createProperty "laenutus-" & gRS("LAENUTUS_ID"), "reference", "lending-copy", "eksemplar-" & gRS("MEEDIA_EKSEMPLAR_FK") & "-1"
        createProperty "laenutus-" & gRS("LAENUTUS_ID"), "date", "lending-lending-date", gRS("LAENUTUS_KUUPAEV")
        createProperty "laenutus-" & gRS("LAENUTUS_ID"), "date", "lending-returning-date", gRS("TAHTAEG_KUUPAEV")
        createProperty "laenutus-" & gRS("LAENUTUS_ID"), "date", "lending-returned-date", gRS("TAGASTUS_KUUPAEV")
        gRS.MoveNext
        moveProgress
    Loop
    
    gRS.Close
    
End Sub

Private Sub deleteEntity(ByVal sEntityOldID)
    Open txtExportFile.Text For Append As #1
    Print #1, "DELETE FROM " & txtDatabase.Text & ".property " _
            & "WHERE created_by = 'v7import' " _
            & "AND entity_id IN (SELECT id FROM " & txtDatabase.Text & ".entity WHERE old_id LIKE '" & sEntityOldID & "%');"
    Print #1, "DELETE FROM " & txtDatabase.Text & ".relationship " _
            & "WHERE created_by = 'v7import' " _
            & "AND relationship_definition_keyname = 'viewer' " _
            & "AND entity_id IN (SELECT id FROM " & txtDatabase.Text & ".entity WHERE old_id LIKE '" & sEntityOldID & "%');"
    Print #1, "DELETE FROM " & txtDatabase.Text & ".entity " _
            & "WHERE created_by = 'v7import' " _
            & "AND old_id LIKE '" & sEntityOldID & "%';"
    Close #1
End Sub

Private Sub createEntity(ByVal sEntityOldID, ByVal sEntityDefinition)
    Open txtExportFile.Text For Append As #1
    Print #1, "INSERT INTO " & txtDatabase.Text & ".entity SET " _
            & "created = NOW(), " _
            & "created_by = 'v7import', " _
            & "old_id = '" & sEntityOldID & "', " _
            & "entity_definition_keyname = '" & sEntityDefinition & "';"
    Print #1, "INSERT INTO " & txtDatabase.Text & ".relationship (old_id, created, created_by, entity_id, related_entity_id, relationship_definition_keyname) " _
            & "SELECT DISTINCT CONCAT(entity.old_id, '-owner-', property.entity_id), NOW(), 'v7import', entity.id, property.entity_id, 'owner' FROM property, entity WHERE property_definition_keyname = 'person-entu-user' AND entity.old_id = '" & sEntityOldID & "';"
    Close #1
End Sub

Private Sub createProperty(ByVal sEntityOldID, ByVal sType, ByVal sPropertyDefinition, ByVal sValue)
    Dim myValue
    sValue = Trim(sValue)
    
    If LenB(sValue) > 0 Then
        Select Case sType
            Case "string"
                With Inet1
                    .AccessType = icUseDefault
                    .Protocol = icHTTPS
                    .Execute "http://arx.ee/chardet?id=" & sEntityOldID & "&property=" & sPropertyDefinition & "&value=" & sValue, "POST", "" & sValue, "Content-Type: text/plain " & vbCrLf
                    While .StillExecuting
                        DoEvents
                    Wend
                End With
                Exit Sub
            Case "integer"
                myValue = "value_integer = " & Replace(sValue & "", ",", ".") & ";"
            Case "decimal"
                myValue = "value_decimal = " & Replace(sValue & "", ",", ".") & ";"
            Case "date"
                myValue = "value_datetime = '" & Format(sValue, "yyyy-mm-dd Hh:Nn:Ss") & "';"
            Case "reference"
                myValue = "value_reference = (SELECT id FROM entity WHERE old_id = '" & sValue & "' LIMIT 1);"
        End Select
    
        Open txtExportFile.Text For Append As #1
        Print #1, "INSERT INTO " & txtDatabase.Text & ".property SET " _
                & "created = NOW(), " _
                & "created_by = 'v7import', " _
                & "entity_id = (SELECT id FROM entity WHERE old_id = '" & sEntityOldID & "' LIMIT 1), " _
                & "property_definition_keyname = '" & sPropertyDefinition & "', " _
                & myValue
        Close #1
    End If

End Sub

Private Sub Inet1_StateChanged(ByVal State As Integer)
    Dim myURL As String
    Dim myBody As String
    Dim sValue As String
    Dim sEntityOldID As String
    Dim sType As String
    Dim sPropertyDefinition As String
    Dim myFile As String
    Dim myOK As Boolean

    If State <> icResponseCompleted Then
        Exit Sub
    End If
    
    myURL = Inet1.URL
    myBody = Inet1.GetChunk(1024, icString)
    
    sEntityOldID = Mid(myURL, InStr(myURL, "id=") + 3, InStr(myURL, "property=") - InStr(myURL, "id=") - 4)
    sPropertyDefinition = Mid(myURL, InStr(myURL, "property=") + 9, InStr(myURL, "value=") - InStr(myURL, "property=") - 10)
    sValue = Trim(Mid(myURL, InStr(myURL, "value=") + 6))
    
    If sValue = "" Then
        Exit Sub
    End If
    
    myFile = Replace(txtExportFile.Text, ".sql", ".error.sql")
    myOK = False
    If Left(myBody, 5) = "EST -" Then
        myFile = txtExportFile.Text
        myOK = True
    End If
    If Left(myBody, 5) = "RUS -" Then
        myFile = Replace(txtExportFile.Text, ".sql", ".rus.sql")
        myOK = True
    End If
    
    If myOK = False Then
        Open myFile For Append As #1
        Print #1, myBody
        Close #1
        Exit Sub
    End If
        
    Open myFile For Append As #1
    Print #1, "INSERT INTO " & txtDatabase.Text & ".property SET " _
            & "created = NOW(), " _
            & "created_by = 'v7import', " _
            & "entity_id = (SELECT id FROM entity WHERE old_id = '" & sEntityOldID & "' LIMIT 1), " _
            & "property_definition_keyname = '" & sPropertyDefinition & "', " _
            & "value_string = '" & Replace(sValue & "", "'", "\'") & "';"
    Close #1

End Sub

Private Sub deleteChild(ByVal sRelationshipOldID)
    Open txtExportFile.Text For Append As #1
    Print #1, "DELETE FROM " & txtDatabase.Text & ".relationship " _
            & "WHERE created_by = 'v7import' " _
            & "AND old_id LIKE '" & sRelationshipOldID & "%';"
    Close #1
End Sub

Private Sub createChild(ByVal sRelationshipOldID, ByVal sEntityOldID, ByVal sRelatedEntityOldID)
    Open txtExportFile.Text For Append As #1
    Print #1, "INSERT INTO " & txtDatabase.Text & ".relationship SET " _
            & "created = NOW(), " _
            & "created_by = 'v7import', " _
            & "old_id = '" & sRelationshipOldID & "', " _
            & "relationship_definition_keyname = 'child', " _
            & "entity_id = (SELECT id FROM entity WHERE old_id = '" & sEntityOldID & "' LIMIT 1), " _
            & "related_entity_id = (SELECT id FROM entity WHERE old_id = '" & sRelatedEntityOldID & "' LIMIT 1);"
    Close #1
End Sub











'Private Sub Export_Inventariraamat()
'    Dim myString As String
'    Dim myN As Integer
'
'    Open Left(txtExportFile.Text, Len(txtExportFile.Text) - 4) & "_INV.csv" For Output As #1
'
'    gRS.Open "SELECT MEEDIA.MEEDIA_LIIK, MEEDIA_EKSEMPLAR.INVENTARI_NUMBER AS INVENTARI_NR, MEEDIA.PEALKIRI, MEEDIA.KLASS, MEEDIA.ILMUMISAASTA, MEEDIA_EKSEMPLAR.NUMBER AS PERIOODIKA_NR, ANDMEKANDJA.NIMI AS ANDMEKANDJA, LIIK.NIMI AS LIIK, KEEL.NIMI AS KEEL, VALJAANDJA.NIMI AS VALJAANDJA, MEEDIA.RIIUL, MEEDIA.MARKUSED AS MEEDIA_MARKUSED, Format([MEEDIA_EKSEMPLAR].[SISSEKANDE_KUUPAEV],""yyyy-mm-dd"") AS SISSEKANDE_KPV, MEEDIA_EKSEMPLAR.HIND, MEEDIA_EKSEMPLAR.KOGUS, SAATEDOKUMENT.DOKUMENDI_NUMBER AS SD_NUMBER, Format([SAATEDOKUMENT].[KUUPAEV],""yyyy-mm-dd"") AS SD_KUUPAEV, VALJAANDJA_1.NIMI AS SD_VALJAANDJA, MAHAKANDMISAKT.AKTI_NUMBER AS MA_NUMBER, Format([MAHAKANDMISAKT].[KUUPAEV],""yyyy-mm-dd"") AS MA_KUUPAEV, MAHAKANDMISAKT.POHJUS AS MA_POHJUS, MEEDIA_EKSEMPLAR.MARKUSED AS EKSEMPLAR_MARKUSED " _
'           & "FROM (((((((MEEDIA_EKSEMPLAR LEFT JOIN MEEDIA ON MEEDIA_EKSEMPLAR.MEEDIA_FK = MEEDIA.MEEDIA_ID) LEFT JOIN VALJAANDJA ON MEEDIA.VALJAANDJA_FK = VALJAANDJA.VALJAANDJA_ID) LEFT JOIN ANDMEKANDJA ON MEEDIA.ANDMEKANDJA_FK = ANDMEKANDJA.ANDMEKANDJA_ID) LEFT JOIN LIIK ON MEEDIA.LIIK_FK = LIIK.LIIK_ID) LEFT JOIN KEEL ON MEEDIA.KEEL_FK = KEEL.KEEL_ID) LEFT JOIN SAATEDOKUMENT ON MEEDIA_EKSEMPLAR.SAATEDOKUMENT_FK = SAATEDOKUMENT.SAATEDOKUMENT_ID) LEFT JOIN VALJAANDJA AS VALJAANDJA_1 ON SAATEDOKUMENT.VALJAANDJA_FK = VALJAANDJA_1.VALJAANDJA_ID) LEFT JOIN MAHAKANDMISAKT ON MEEDIA_EKSEMPLAR.MAHAKANDMISAKT_FK = MAHAKANDMISAKT.MAHAKANDMISAKT_ID " _
'           & "ORDER BY MEEDIA.MEEDIA_LIIK, TRIM(MEEDIA_EKSEMPLAR.INVENTARI_NUMBER), TRIM(MEEDIA.PEALKIRI), TRIM(MEEDIA.KLASS)", gConnect
'
'    myString = ""
'    For myN = 0 To gRS.Fields.Count - 1
'        myString = myString & ";" & gRS(myN).Name
'    Next myN
'    Print #1, Mid(myString, 2)
'
'    Do Until gRS.EOF
'
'        myString = ""
'        For myN = 0 To gRS.Fields.Count - 1
'            If IsNull(gRS(myN)) Then
'                myString = myString & ";"
'            Else
'                myString = myString & ";" & IIf(IsNull(Trim(gRS(myN))) = True, "", Replace(Trim(gRS(myN)), ";", ","))
'            End If
'        Next myN
'
'        Print #1, Mid(myString, 2)
'
'        gRS.MoveNext
'    Loop
'    gRS.Close
'
'    Close #1
'
'End Sub

